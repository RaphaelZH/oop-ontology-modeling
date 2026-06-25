from owlready2 import *
from pyswip import Prolog
import types

from DictionaryGenerator import python_dictionary_generator
from BasicClassGenerator import ontology_generator

keywords_dict, operators_dict, other_symbols_dict = python_dictionary_generator()

onto = ontology_generator()


def prop_syntactic_chain(cls):
    global onto
    with onto:
        for i in range(1, len(list(cls.subclasses())) + 1):
            exec(
                f"{onto}.{cls.name}{i}('{cls.name[:-4]}_ind{i}', \
                    equivalent_to = {onto}.{cls.name}{i}.equivalent_to[0].instances())"
            )
            exec(
                f"{onto}.{cls.name[:-4]}_ind.syntax_container.append\
                    ({onto}.{cls.name[:-4]}_ind{i})"
            )
            if i == 1:
                exec(
                    f"{onto}.{cls.name[:-4]}_ind.syntactic_chain = \
                        [{onto}.{cls.name[:-4]}_ind{i}]"
                )
            else:
                j = i - 1
                exec(
                    f"{onto}.{cls.name[:-4]}_ind{j}.syntactic_chain = \
                        [{onto}.{cls.name[:-4]}_ind{i}]"
                )


    """
    for key, value in keywords_dict.items():
        exec(
            f"types.new_class('python_{key}', \
                tuple([python_keywords]))"
        )
        exec(
            f"onto.python_{key}('python_{key.lower()}', \
                specific_language=onto.python, \
                    string_value='{value}')"
        )
    """

with onto:

    class specific_language(ObjectProperty, FunctionalProperty):
        domain = [onto.language_grammar]
        range = [onto.programming_language]

    class python(onto.programming_language):
        pass

    class python_lexer(onto.language_lexer):
        pass

    class python_keywords(python_lexer):
        pass

    class python_operators(python_lexer):
        pass

    class python_other_symbols(python_lexer):
        pass

    for key, value in keywords_dict.items():
        exec(
            f"types.new_class('python_{key}', \
                tuple([python_keywords]))"
        )
        exec(
            f"onto.python_{key}('python_{key.lower()}', \
                specific_language=onto.python, \
                    string_value='{value}')"
        )

    for key, value in operators_dict.items():
        exec(
            f"types.new_class('python_{key}', \
                tuple([python_operators]))"
        )
        exec(
            f"onto.python_{key}('python_{key.lower()}', \
                specific_language=onto.python, \
                    string_value='{value}')"
        )

    for key, value in other_symbols_dict.items():
        exec(
            f"types.new_class('python_{key}', \
                tuple([python_other_symbols]))"
        )
        exec(
            f"onto.python_{key}('python_{key.lower()}', \
                specific_language=onto.python, \
                    string_value='{value}')"
        )

    class python_parser(onto.language_parser):
        pass

    class python_arguments(python_parser):
        pass

    class python_arglist_cls(python_parser):
        pass

    ### test
    python_arglist_cls("python_arglist_ind", specific_language=onto.python)

    class python_stmt(python_parser):
        pass

    class python_simple_stmt(python_stmt):
        pass

    class python_compound_stmt(python_stmt):
        pass

    class python_suite(python_parser):
        pass

    class python_suite1_cls(python_suite):
        pass

    class python_suite2_cls(python_suite):
        pass

    python_suite2_ind = python_suite2_cls(
        "python_suite2_ind", specific_language=onto.python
    )

    class python_suite2_cls1(python_suite2_cls):
        equivalent_to = [onto.python_LINE_BREAK]

    class python_suite2_cls2(python_suite2_cls):
        equivalent_to = [onto.python_INDENT]

    class python_suite2_cls3(python_suite2_cls):
        equivalent_to = [onto.python_DEDENT]

    prop_syntactic_chain(python_suite2_cls)

    ### test
    # python_suite_cls("python_suite_ind", specific_language=onto.python)

    # class python_suite_syn1(python_suite):
    #    equivalent_to = [python_simple_stmt]

    class python_classdef_cls(python_parser):
        pass

    python_classdef_ind = python_classdef_cls(
        "python_classdef_ind", specific_language=onto.python
    )

    class python_classdef_cls1(python_classdef_cls):
        equivalent_to = [onto.python_CLASS]

    class python_classdef_cls2(python_classdef_cls):
        equivalent_to = [onto.variable_name]

    class python_classdef_cls3(python_classdef_cls):
        equivalent_to = [python_arglist_cls]

    class python_classdef_cls4(python_classdef_cls):
        equivalent_to = [onto.python_COLON]

    class python_classdef_cls5(python_classdef_cls):
        equivalent_to = [python_suite2_cls]

    prop_syntactic_chain(python_classdef_cls)

    class python_funcdef(python_parser):
        pass


for ind in onto.individuals():
    if ind.equivalent_to != []:
        for prop in ind.equivalent_to[0].get_properties():
            exec(
                f"onto.{ind.name}.{prop.name} = onto.{ind.equivalent_to[0].name}.{prop.name}"
            )
        if ind.string_value is None:
            variable_text = "{" + ind.equivalent_to[0].name + "}"
            exec(f"onto.{ind.name}.string_value = '{variable_text}'")

onto.save(file="1. Ontology Files/Programming Language Parser.owl")

del onto

prolog = Prolog()
prolog.assertz("ancestor(A, D) :- parent(A, D)")
prolog.assertz("ancestor(A, D) :- parent(A, P), ancestor(P, D)")

onto = get_ontology("1. Ontology Files/Programming Language Parser.owl").load()


stmt_list = ["python_classdef_ind", "python_suite2_ind"]
# It may be necessary to develop it as a function or class in the future. --------------------------
with onto:
    for individual in onto.individuals():
        if individual.name in stmt_list:
            prolog.assertz(
                f"parent({individual.name}, {individual.syntactic_chain[0].name})"
            )
            for ind in individual.syntax_container:
                if len(ind.syntactic_chain) > 0:
                    prolog.assertz(f"parent({ind.name}, {ind.syntactic_chain[0].name})")
                # print(ind.string_value)
    descendant_list = []
    for q in prolog.query("ancestor(python_classdef_ind, X)"):
        exec(f"descendant_list.append(onto.{q['X']}.string_value)")

    print(" ".join(descendant_list))
# --------------------------------------------------------------------------------------------------
