import random, math, pickle
import ast as a

class ASTObj():
    def __repr__(self): return "\\AST"

BYTES_ENCODING = "ISO-8859-1"

def obfuscate(code):

    #output = "# Obfuscated by Mystical - Good Luck!\n"
    output = ""

    # Create names of classes
    utility_class_id, char_storage_class_id, runtime_class_id, ast_wrapper_class_id, number_class_id, built_ast_id, pickled_objects, ast_obj_filler_class_id = random.sample(["_", "__", "___", "____", "_____", "______", "_______", "________"], 8)

    # Use class definitions for temporary lambdas 
    output += f"{utility_class_id}=lambda _:type(*_);_0_=str;{runtime_class_id}=dict;"

    # Create zero, one, and two
    zero_name, one_name, two_name = random.sample(["_", "__", "___"], 3)
    zero, one, two = f"{number_class_id}.{zero_name}", f"{number_class_id}.{one_name}", f"{number_class_id}.{two_name}"
    output += f"_0=lambda _0:_0.__code__.co_argcount;{built_ast_id}=None;__0=_0;{number_class_id}={utility_class_id}([_0_(),(),{runtime_class_id}("
    numbers = [f"{zero_name}=_0(lambda:__0)", f"{one_name}=_0(lambda _0:_0)", f"{two_name}=_0(lambda _0,__0:_0)"]
    output += ",".join(random.sample(numbers, len(numbers))) + f")]);{pickled_objects}=[];"

    # Find closest square root
    def nearest_sqrt(number):
        floor_sqrt = math.floor(math.sqrt(number))
        ceil_sqrt = math.floor(math.sqrt(number))
        floor_diff, ceil_diff = number - floor_sqrt, ceil_sqrt - number
        return floor_sqrt if floor_diff >= ceil_diff else ceil_sqrt

    # Function to create numbers using zero, one, and two
    def create_sqrt_number(number):
        if number < 3:
            return str(number)
        num_sqrt = nearest_sqrt(number)
        nearest_perfect_square = num_sqrt ** 2
        distance = abs(number - nearest_perfect_square)
        symbol = "+" if number > nearest_perfect_square else ("-" if number < nearest_perfect_square else None)
        if symbol == None:
            return f"{create_sqrt_number(num_sqrt)}**2"
        else:
            return f"({create_sqrt_number(num_sqrt)}**2{symbol}{create_sqrt_number(distance) if distance > 2 else distance})"

    # Function to create integers using prime factorization
    def create_number(number):
        if number == 0:
            return zero
        if number == 1:
            return one
        factors = []
        while number % 2 == 0:
            factors.append(2)
            number //= 2
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            while number % i == 0:
                factors.append(i)
                number //= i
        if number > 2:
            factors.append(number)
        return_string = "*".join(f"{create_sqrt_number(n)}" for n in factors) if len(factors) > 1 else create_sqrt_number(factors[0])
        return return_string.replace("0", zero).replace("1", one).replace("2", two)
    
    # Generate the utility class
    output += f"{utility_class_id}={utility_class_id}([_0_(),(),{runtime_class_id}("

    # Utility class functions
    u_blank_string, u_getattr, u_getbuiltin, u_create_type, u_dict, u_globals, u_class, u_dir, u_name, u_ge, u_iter, u_int, u_float, u_complex, u_ord, u_True, u_empty_list, u_empty_dict, u_chr, u_hex, u_equals_comp, u_pow, u_str, u_reversed, u_file = random.sample(["_" + "_" * i for i in range(25)], 25)
    utility_class_functions = [
        f"{u_blank_string}=lambda:{utility_class_id}.{u_getbuiltin}({utility_class_id}.{u_name}({utility_class_id}.{u_class}({utility_class_id}.{u_empty_list}()))[{create_number(2)}:{create_number(4)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(3)}])()",
        f"{u_getattr}=lambda _0,__0:{utility_class_id}.{u_getbuiltin}({utility_class_id}.{u_name}({utility_class_id}.{u_ge}({utility_class_id}.{u_int}()))[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(1)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_float}())[{create_number(3)}]+({utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(1)}]*{create_number(2)})+{utility_class_id}.{u_name}({utility_class_id}.{u_ord}())[{create_number(1)}])(_0,__0)",
        f"{u_getbuiltin}=lambda _0:getattr({utility_class_id}.{u_globals}()()[{utility_class_id}.{u_name}({utility_class_id}.{u_dir}(()))[{create_number(1)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_dir}(()))[{create_number(1)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}({utility_class_id}.{u_True}()))[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}(({utility_class_id},)))[{create_number(1)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}({utility_class_id}.{u_empty_list}()))[{create_number(1)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}({utility_class_id}.{u_empty_list}()))[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}({utility_class_id}.{u_empty_list}()))[{create_number(3)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}({utility_class_id}.{u_int}()()))[:{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}({utility_class_id}.{u_empty_list}()))[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_dir}(()))[{create_number(1)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_dir}(()))[{create_number(1)}]],_0)",
        f"{u_chr}=lambda _0:{utility_class_id}.{u_getbuiltin}({utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_hex}())[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(3)}])(_0)",
        f"{u_reversed}=lambda:{utility_class_id}.{u_getbuiltin}({utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(3)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(2)}]+{utility_class_id}.{u_chr}({create_number(118)})+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(3)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}({utility_class_id}.{u_empty_list}()))[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}({utility_class_id}.{u_empty_dict}()))[{create_number(0)}])",
        f"{u_create_type}=lambda _0:{utility_class_id}.{u_getbuiltin}({utility_class_id}.{u_name}({utility_class_id}.{u_class}(type({utility_class_id}.{u_blank_string}()))))(*_0)",
        f"{u_equals_comp}=lambda _0,__0:_0==__0",
        f"{u_globals}=lambda:globals",
        f"{u_dict}=lambda:{utility_class_id}.{u_getbuiltin}({utility_class_id}.{u_name}({utility_class_id}.{u_class}({utility_class_id}.{u_empty_dict}())))",
        f"{u_class}=lambda _:_.__class__",
        f"{u_dir}=lambda _:_.__dir__",
        f"{u_name}=lambda _:_.__name__",
        f"{u_ge}=lambda _:_.__ge__",
        f"{u_file}=lambda:__file__",
        f"{u_iter}=lambda:iter",
        f"{u_int}=lambda:{utility_class_id}.{u_class}({create_number(0)})",
        f"{u_float}=lambda:float",
        f"{u_complex}=lambda:complex",
        f"{u_ord}=lambda:ord",
        f"{u_True}=lambda:{utility_class_id}.{u_equals_comp}({utility_class_id},{utility_class_id})",
        f"{u_empty_list}=lambda:[]",
        f"{u_empty_dict}=lambda:{{}}",
        f"{u_hex}=lambda:hex",
        f"{u_pow}=lambda:pow",
        f"{u_str}=lambda:str"
    ]
    output += ",".join(random.sample(utility_class_functions, len(utility_class_functions))) + ")]);"

    # Execute "import pickle"
    output += f"{utility_class_id}.{u_getbuiltin}({utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_hex}())[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(0)}])({utility_class_id}.{u_name}({utility_class_id}.{u_class}([]))[{create_number(1)}]+{utility_class_id}.{u_chr}({create_number(109)})+{utility_class_id}.{u_name}({utility_class_id}.{u_pow}())[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_ord}())[{create_number(0)}:{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}([]))[{create_number(3)}]+{utility_class_id}.{u_chr}({create_number(32)})+{utility_class_id}.{u_name}({utility_class_id}.{u_pow}())[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(0)}]+{utility_class_id}.{u_chr}({create_number(107)})+{utility_class_id}.{u_name}({utility_class_id}.{u_class}([]))[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]);"

    # Create AST object class for use in the array
    output += f"{ast_obj_filler_class_id}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()()]);"

    # Create wrapper class for AST
    output += f"{ast_wrapper_class_id}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()("

    a_create_exec_path, a_walk_pickled_objects, a_undo_pickling, a_do_exec, a_get_global_decl, a_semicolon, a_underscore, a_quote, a_equals_pickle_loads, a_open_paren, a_close_paren, a_string_join, a_open_bracket, a_close_bracket, a_period, a_hyphen, a_do_iso_encoding = random.sample(["_" + "_" * i for i in range(17)], 17)

    # AST class functions
    ast_class_functions = [
        f"{a_do_exec}=lambda _0,__0:{utility_class_id}.{u_getbuiltin}({utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_hex}())[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(0)}])(_0)",
        f"{a_equals_pickle_loads}=lambda:{utility_class_id}.{u_chr}({create_number(61)})+{utility_class_id}.{u_name}({utility_class_id}.{u_pow}())[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(0)}]+{utility_class_id}.{u_chr}({create_number(107)})+{utility_class_id}.{u_name}({utility_class_id}.{u_class}([]))[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_chr}({create_number(46)})+{utility_class_id}.{u_name}({utility_class_id}.{u_class}([]))[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(1)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_float}())[{create_number(3)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_ord}())[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_globals}())[-{create_number(1)}]",
        f"{a_do_iso_encoding}=lambda _0:{utility_class_id}.{u_getattr}(_0,{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_int}())[{create_number(1)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_ord}())[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_ord}())[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}])({utility_class_id}.{u_chr}({create_number(73)})+{utility_class_id}.{u_chr}({create_number(83)})+{utility_class_id}.{u_chr}({create_number(79)})+{ast_wrapper_class_id}.{a_hyphen}()+{utility_class_id}.{u_str}()({create_number(8859)})+{ast_wrapper_class_id}.{a_hyphen}()+{utility_class_id}.{u_str}()({create_number(1)}))",
        f"{a_string_join}=lambda:{utility_class_id}.{u_getattr}({utility_class_id}.{u_str}()(),{utility_class_id}.{u_chr}({create_number(106)})+{utility_class_id}.{u_name}({utility_class_id}.{u_pow}())[{create_number(1)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(0)}]+{utility_class_id}.{u_chr}({create_number(110)}))",
        f"{a_create_exec_path}=lambda _0:({ast_wrapper_class_id}.{a_underscore}()*{create_number(len(built_ast_id))})+{ast_wrapper_class_id}.{a_string_join}()(({ast_wrapper_class_id}.{a_open_bracket}()+{utility_class_id}.{u_str}()(__0)+{ast_wrapper_class_id}.{a_close_bracket}())if({utility_class_id}.{u_equals_comp}({utility_class_id}.{u_create_type}([__0]),{utility_class_id}.{u_int}()))else(({ast_wrapper_class_id}.{a_period}()+__0)if({utility_class_id}.{u_equals_comp}({utility_class_id}.{u_create_type}([__0]),{utility_class_id}.{u_str}()))else({utility_class_id}.{u_str}()()))for(__0)in(_0))",
        f"{a_get_global_decl}=lambda:{utility_class_id}.{u_name}({utility_class_id}.{u_globals}())[:-{create_number(1)}]+{utility_class_id}.{u_chr}({create_number(32)})+{ast_wrapper_class_id}.{a_underscore}()*({create_number(len(built_ast_id))})+{ast_wrapper_class_id}.{a_semicolon}()",
        f"{a_walk_pickled_objects}=lambda:[{ast_wrapper_class_id}.{a_undo_pickling}(_0,{ast_wrapper_class_id}.{a_do_iso_encoding}(__0))for(_0,__0)in({utility_class_id}.{u_reversed}()({pickled_objects}))]",
        f"{a_undo_pickling}=lambda _0,__0:{ast_wrapper_class_id}.{a_do_exec}({ast_wrapper_class_id}.{a_get_global_decl}()+{ast_wrapper_class_id}.{a_create_exec_path}(_0)+{ast_wrapper_class_id}.{a_equals_pickle_loads}()+{ast_wrapper_class_id}.{a_open_paren}()+({ast_wrapper_class_id}.{a_underscore}()*{create_number(2)})+{utility_class_id}.{u_str}()({create_number(0)})+{ast_wrapper_class_id}.{a_close_paren}(),__0)",
        f"{a_semicolon}=lambda:{utility_class_id}.{u_chr}({create_number(59)})",
        f"{a_underscore}=lambda:{utility_class_id}.{u_chr}({create_number(95)})",
        f"{a_quote}=lambda:{utility_class_id}.{u_chr}({create_number(34)})",
        f"{a_open_paren}=lambda:{utility_class_id}.{u_chr}({create_number(40)})",
        f"{a_close_paren}=lambda:{utility_class_id}.{u_chr}({create_number(41)})",
        f"{a_open_bracket}=lambda:{utility_class_id}.{u_chr}({create_number(91)})",
        f"{a_close_bracket}=lambda:{utility_class_id}.{u_chr}({create_number(93)})",
        f"{a_period}=lambda:{utility_class_id}.{u_chr}({create_number(46)})",
        f"{a_hyphen}=lambda:{utility_class_id}.{u_chr}({create_number(45)})"
    ]
    output += ",".join(ast_class_functions) + ")]);"

    objs = get_pickled_object_list(code)

    # Create character storage class and its subclasses
    output += f"{char_storage_class_id}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()("
    c_subclass_pathstrings, c_subclass_pathints, c_subclass_chars, c_subclass_bytes, c_subclass_pathlists = random.sample(["_", "__", "___", "____", "_____"], 5)
    char_storage_subclasses = ["", "", "", "", ""]

    # Characters for Strings/Bytes
    char_storage_subclasses[0] += f"{c_subclass_chars}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()("
    CHAR_CLASS_SPLITS = 20
    required_characters = get_required_characters(objs)
    split_class_required_characters = chunkify(required_characters, CHAR_CLASS_SPLITS)
    split_class_required_characters_ids = random.sample(["_" + "_" * i for i in range(CHAR_CLASS_SPLITS)], CHAR_CLASS_SPLITS)

    character_method_mapping = {}
    for index, char_list in enumerate(split_class_required_characters):
        individual_character_variables = random.sample(["_" + "_" * i for i in range(len(char_list))], len(char_list))
        for char_index, char in enumerate(char_list):
            character_method_mapping[char] = [split_class_required_characters_ids[index], individual_character_variables[char_index]]

    character_subclass_list = ["" for _ in range(CHAR_CLASS_SPLITS)]
    for index, character_subclass in enumerate(split_class_required_characters):
        character_subclass_list[index] += f"{split_class_required_characters_ids[index]}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()("

        individual_characters = [f"{character_method_mapping[char][-1]}={utility_class_id}.{u_chr}({create_number(ord(char))})" for char in character_subclass]
        character_subclass_list[index] += ",".join(random.sample(individual_characters, len(individual_characters))) + ")])"
    char_storage_subclasses[0] += ",".join(random.sample(character_subclass_list, len(character_subclass_list))) + ")])"

    # Path Strings
    char_storage_subclasses[1] += f"{c_subclass_pathstrings}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()("
    required_strings = get_required_path_strings(objs)
    required_strings_ids = random.sample(["_" + "_" * i for i in range(len(required_strings))], len(required_strings))
    string_method_mapping = {}

    char_storage_pathstring_items = []
    for i in range(len(required_strings)):
        string_method_mapping[required_strings[i]] = required_strings_ids[i]
        string_content = "+".join(f"{char_storage_class_id}.{c_subclass_chars}.{'.'.join(character_method_mapping[ch])}" for ch in required_strings[i])
        char_storage_pathstring_items.append(f"{required_strings_ids[i]}=lambda:{string_content}")
    char_storage_subclasses[1] += ",".join(random.sample(char_storage_pathstring_items, len(char_storage_pathstring_items))) + ")])"

    # Path Integers
    char_storage_subclasses[2] += f"{c_subclass_pathints}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()("
    required_integers = get_required_path_integers(objs)
    required_integers_ids = random.sample(["_" + "_" * i for i in range(len(required_integers))], len(required_integers))
    integer_method_mapping = {}
    for i, integer in enumerate(required_integers):
        integer_method_mapping[integer] = required_integers_ids[i]
    
    char_storage_pathint_items = [f"{required_integers_ids[i]}={create_number(required_integers[i])}" for i in range(len(required_integers))]
    char_storage_subclasses[2] += ",".join(random.sample(char_storage_pathint_items, len(char_storage_pathint_items))) + ")])"

    # Byte Arrays
    char_storage_subclasses[3] += f"{c_subclass_bytes}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()("
    BYTE_CLASS_SPLITS = 20
    required_bytes = list(set(get_all_bytestrings(objs)))
    split_class_required_bytes = chunkify(required_bytes, BYTE_CLASS_SPLITS)
    split_class_required_bytes_ids = random.sample(["_" + "_" * i for i in range(BYTE_CLASS_SPLITS)], BYTE_CLASS_SPLITS)
    
    bytes_method_mapping = {}
    for index, byte_list in enumerate(split_class_required_bytes):
        individual_byte_variables = random.sample(["_" + "_" * i for i in range(len(byte_list))], len(byte_list))
        for byte_index, byte_string in enumerate(byte_list):
            bytes_method_mapping[byte_string] = [split_class_required_bytes_ids[index], individual_byte_variables[byte_index]]
        
    byte_subclass_list = ["" for _ in range(BYTE_CLASS_SPLITS)]
    for index, byte_subclass in enumerate(split_class_required_bytes):
        byte_subclass_list[index] += f"{split_class_required_bytes_ids[index]}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()("
        
        individual_byte_strings = []
        for byte_string in byte_subclass:
            string_content = "+".join(f"{char_storage_class_id}.{c_subclass_chars}.{'.'.join(character_method_mapping[char])}" for char in byte_string)
            individual_byte_strings.append(f"{bytes_method_mapping[byte_string][-1]}=lambda:{string_content}")
        
        byte_subclass_list[index] += ",".join(random.sample(individual_byte_strings, len(individual_byte_strings))) + ")])"
    char_storage_subclasses[3] += ",".join(random.sample(byte_subclass_list, len(byte_subclass_list))) + ")])"

    # Path Lists
    char_storage_subclasses[4] += f"{c_subclass_pathlists}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()("
    PATHLIST_CLASS_SPLITS = 20
    required_pathlists = get_required_pathlists(objs)
    split_class_required_pathlists = chunkify(required_pathlists, PATHLIST_CLASS_SPLITS)
    split_class_required_pathlists_ids = random.sample(["_" + "_" * i for i in range(PATHLIST_CLASS_SPLITS)], PATHLIST_CLASS_SPLITS)

    pathlist_method_mapping = {}
    for index, pathlist_list in enumerate(split_class_required_pathlists):
        individual_pathlist_variables = random.sample(["_" + "_" * i for i in range(len(pathlist_list))], len(pathlist_list))
        for path_index, path_list in enumerate(pathlist_list):
            pathlist_method_mapping[str(path_list)] = [split_class_required_pathlists_ids[index], individual_pathlist_variables[path_index]]

    pathlist_subclass_list = ["" for _ in range(PATHLIST_CLASS_SPLITS)]
    for index, pathlist_subclass in enumerate(split_class_required_pathlists):
        pathlist_subclass_list[index] += f"{split_class_required_pathlists_ids[index]}={utility_class_id}.{u_create_type}([{utility_class_id}.{u_blank_string}(),(),{utility_class_id}.{u_dict}()("

        individual_pathlist_strings = []
        for path_list in pathlist_subclass:
            list_items = [ast_obj_filler_class_id if type(item) == ASTObj else (f"{char_storage_class_id}.{c_subclass_pathstrings}.{string_method_mapping[item]}()" if type(item) == str else f"{char_storage_class_id}.{c_subclass_pathints}.{integer_method_mapping[item]}") for item in path_list]
            string_content = "[" + ",".join(list_items) + "]"
            individual_pathlist_strings.append(f"{pathlist_method_mapping[str(path_list)][-1]}=lambda:{string_content}")
        
        pathlist_subclass_list[index] += ",".join(random.sample(individual_pathlist_strings, len(individual_pathlist_strings))) + ")])"
    char_storage_subclasses[4] += ",".join(random.sample(pathlist_subclass_list, len(pathlist_subclass_list))) + ")])"

    output += ",".join(random.sample(char_storage_subclasses, len(char_storage_subclasses))) + ")]);"

    array_items = []
    for path, byte_string in objs:
        item_string = f"({char_storage_class_id}.{c_subclass_pathlists}.{'.'.join(p for p in pathlist_method_mapping[str(path)])}(),{char_storage_class_id}.{c_subclass_bytes}.{'.'.join(p for p in bytes_method_mapping[byte_string.decode(BYTES_ENCODING)])}())"
        array_items.append(item_string)
    output += f"{pickled_objects}=[{','.join(array_items)}];"

    output += f"{ast_wrapper_class_id}.{a_walk_pickled_objects}();"

    output += f"{utility_class_id}.{u_getbuiltin}({utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_hex}())[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(0)}])({utility_class_id}.{u_getbuiltin}({utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[:{create_number(4)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_iter}())[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_class}([]))[{create_number(0)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}])({built_ast_id},{utility_class_id}.{u_file}(),{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_hex}())[{create_number(2)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(5)}]+{utility_class_id}.{u_name}({utility_class_id}.{u_complex}())[{create_number(0)}]))"

    return output

def chunkify(lst, n):
    return [lst[i::n] for i in range(n)]

def get_compressed_path_list(path_list):
    paths = []
    [paths.extend(p) for p in [path for path, _ in path_list]]
    return paths

def get_required_path_strings(pickled_objects):
    paths = get_compressed_path_list(pickled_objects)
    return list(set(filter(lambda item: type(item) == str, paths)))

def get_required_path_integers(pickled_objects):
    paths = get_compressed_path_list(pickled_objects)
    return list(set(filter(lambda item: type(item) == int, paths)))

def get_all_bytestrings(pickled_objects):
    return [bts.decode(BYTES_ENCODING) for _, bts in pickled_objects]

def get_required_characters(pickled_objects):
    string_list = "".join(get_required_path_strings(pickled_objects))
    bytes_list = "".join(get_all_bytestrings(pickled_objects))
    return list(set(string_list + bytes_list))

def get_required_pathlists(pickled_objects):
    return [path_list for path_list, _ in pickled_objects]

def get_pickled_object_list(code):

    global ast
    ast = a.parse(code)
    visited = []

    def walk_ast_dict(obj, path):
        if isinstance(obj, a.AST):
            visited.append(path)
            field_dict = {}
            for key, value in obj.__dict__.items():
                if key in obj._fields:
                    field_dict[key] = value
            walk_ast_dict(field_dict, path + [ASTObj()])
        elif type(obj) == dict:
            for key, value in obj.items():
                walk_ast_dict(value, path + [key])
        elif type(obj) == list:
            for index, item in enumerate(obj):
                walk_ast_dict(item, path + [index])

    def get_exec_path(path):
        access_string = "ast"
        for item in path:
            if type(item) == int:
                access_string += f"[{item}]"
            elif type(item) == str:
                access_string += f".{item}"
        return access_string

    already_deleted_paths = []
    pickled_objects = []

    def pickle_ast_object(path):
        obj_to_pickle = eval(get_exec_path(path))
        pickled_objects.append((path, pickle.dumps(obj_to_pickle)))

    def delete_ast_item_at_path(path):
        if path == []:
            exec("global ast;ast=None")
        else:
            exec(get_exec_path(path) + "=None")
        already_deleted_paths.append(path)

    def recursively_pickle(path):
        target_index = max(index for index, item in enumerate(path) if type(item) == ASTObj) if len(path) > 0 else None
        item_path = path[:target_index]
        if not item_path in already_deleted_paths:
            pickle_ast_object(item_path)
            delete_ast_item_at_path(item_path)

    walk_ast_dict(ast, [])
    ordered = sorted(visited, key=len)
    for path in reversed(ordered):
        recursively_pickle(path)

    return pickled_objects

if __name__ == "__main__":
    data = open("Files/In.py", "r").read()
    # random.seed(data)
    output = obfuscate(data)
    with open("Files/Out.py", "w+") as f:
        f.write(output)
