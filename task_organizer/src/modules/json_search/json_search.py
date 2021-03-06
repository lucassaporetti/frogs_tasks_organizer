import re

from idna.core import unicode

RE_JSON_NAME = '[a-zA-Z0-9_\\- ]'
RE_JSON_ARRAY_INDEX = '[0-9]{1,}'


class JsonSearch:

    # Construction
    def __init__(self, separator='.', json_name_re=RE_JSON_NAME, json_array_index_re=RE_JSON_ARRAY_INDEX):
        self.separator = separator
        self.jsonNameRe = json_name_re
        self.jsonArrayIndexRe = json_array_index_re
        self.pat_elem = None
        self.pat_sel_elem_val = None
        self.pat_sub_expr = None
        self.pat_sub_expr_val = None

    # find the next element in the list matching the specified value.
    def __find_next_element__(self, root_element, match_name, match_value=None, fetch_parent=False):
        selected_element = root_element
        if type(selected_element) is list:
            for nextInList in root_element:
                if type(nextInList) is dict:
                    selected_element = nextInList.get(match_name)
                    if selected_element and (match_value is None or (match_value and selected_element == match_value)):
                        # To return the parent element instead of the leaf
                        if fetch_parent:
                            selected_element = nextInList
                        break
                    else:
                        selected_element = None
                elif type(nextInList) is unicode:
                    selected_element = root_element
                elif type(nextInList) is list:
                    selected_element = self.__find_next_element__(nextInList, match_name, match_value)
        elif type(selected_element) is dict:
            el = selected_element.get(match_name)
            if el and (match_value is None or (match_value and el == match_value)):
                # To return the parent element instead of the leaf
                if not fetch_parent:
                    selected_element = el
            else:
                selected_element = None
        else:
            selected_element = None

        return selected_element

    # Find the element in the sub-expressions.
    def __find_in_subex__(self, sub_expressions, sub_selected_element, pat_subst_expr_val, fetch_parent=False):
        for nextSubExpr in sub_expressions:

            if nextSubExpr:
                sub_parts = re.search(pat_subst_expr_val, nextSubExpr)
                sub_elem_id = sub_parts.group(1)
                sub_elem_val = sub_parts.group(3)
                sub_selected_element = self.__find_next_element__(
                    sub_selected_element, sub_elem_id, sub_elem_val, fetch_parent)

        return sub_selected_element

    # Purpose: Get the json element through it's path. Returned object is either [dict, list or unicode].
    #
    #   Search patterns:
    #     elem1.elem2
    #     elem1.elem2[index]
    #     elem1.elem2{property}
    #     elem1.elem2{property}[index]
    #     elem1.elem2{property<value>}
    #     elem1.elem2[index].elem3
    #     elem1.elem2{property}.elem3
    #     elem1.elem2{property<value>}.elem3
    #     elem1.elem2{property<value>}[index].elem3
    #     elem1.elem2{property<value>}.{property2<value2>}.elem3
    def json_select(self, root_element, search_path, fetch_parent=False):
        self.pat_elem = '%s+' % self.jsonNameRe
        self.pat_sel_elem_val = '(%s)?((\\{(%s)(<(%s)>)?\\})+)(\\[(%s)\\])?' % (
            self.pat_elem, self.pat_elem, self.pat_elem, self.jsonArrayIndexRe)
        self.pat_sub_expr = '(\\{%s\\})' % self.pat_elem
        self.pat_sub_expr_val = '\\{(%s)(<(%s)>)?\\}' % (self.pat_elem, self.pat_elem)
        selected_element = root_element
        try:
            search_tokens = search_path.split(self.separator)
            for nextElement in search_tokens:
                if nextElement.find('{') >= 0:  # Next element has nested elements
                    parts = re.search(self.pat_sel_elem_val, nextElement)
                    sel_elem_id = parts.group(1)
                    sub_parts = parts.group(2)
                    elem_array_group = parts.group(7)
                    elem_array_index = parts.group(8)
                    sub_expressions = re.compile(self.pat_sub_expr).split(sub_parts)
                    if sel_elem_id and type(selected_element) is dict:
                        selected_element = selected_element.get(sel_elem_id)
                    if selected_element:
                        # Our first element is a list, so we will have to loop and find all the elements
                        # and sub expressions in it.
                        if type(selected_element) is list:
                            for nextInList in selected_element:
                                sub_selected_element = self.__find_in_subex__(
                                    sub_expressions, nextInList, self.pat_sub_expr_val, fetch_parent)
                                # It sub_selected_element is not null then we have found what we wanted.
                                if sub_selected_element:
                                    selected_element = sub_selected_element
                                    break
                        # Check if there are indexed elements.
                        if elem_array_group and elem_array_index and type(selected_element) is list:
                            selected_element = selected_element[int(elem_array_index)]

                elif nextElement.find('[') >= 0:  # Next element is indexed
                    pat_sel_elem_idx = '(%s)\\[(%s)\\]' % (self.pat_elem, self.jsonArrayIndexRe)
                    parts = re.search(pat_sel_elem_idx, nextElement)
                    sub_elem_id = parts.group(1)
                    elem_array_index = parts.group(2)
                    # TODO Implement subarrays like elem[0][1][2]
                    if sub_elem_id is not None and elem_array_index is not None:
                        el = selected_element.get(sub_elem_id)
                        if type(el) is list:
                            selected_element = el[int(elem_array_index)]
                else:  # Next element is simple
                    selected_element = selected_element.get(nextElement)
        except (AttributeError, IndexError):
            selected_element = None
            pass

        return selected_element
