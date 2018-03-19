# Copyright 2017 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "SHORT_EXTERNAL_STRING_TYPE",
  106: "SHORT_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_BIGINT64_ARRAY_TYPE",
  149: "FIXED_BIGUINT64_ARRAY_TYPE",
  150: "FIXED_DOUBLE_ARRAY_TYPE",
  151: "FEEDBACK_METADATA_TYPE",
  152: "FILLER_TYPE",
  153: "ACCESS_CHECK_INFO_TYPE",
  154: "ACCESSOR_INFO_TYPE",
  155: "ACCESSOR_PAIR_TYPE",
  156: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "ALLOCATION_SITE_TYPE",
  159: "ASYNC_GENERATOR_REQUEST_TYPE",
  160: "CONTEXT_EXTENSION_TYPE",
  161: "DEBUG_INFO_TYPE",
  162: "FUNCTION_TEMPLATE_INFO_TYPE",
  163: "INTERCEPTOR_INFO_TYPE",
  164: "MODULE_INFO_ENTRY_TYPE",
  165: "MODULE_TYPE",
  166: "OBJECT_TEMPLATE_INFO_TYPE",
  167: "PROMISE_CAPABILITY_TYPE",
  168: "PROMISE_REACTION_TYPE",
  169: "PROTOTYPE_INFO_TYPE",
  170: "SCRIPT_TYPE",
  171: "STACK_FRAME_INFO_TYPE",
  172: "TUPLE2_TYPE",
  173: "TUPLE3_TYPE",
  174: "WASM_COMPILED_MODULE_TYPE",
  175: "WASM_DEBUG_INFO_TYPE",
  176: "WASM_SHARED_MODULE_DATA_TYPE",
  177: "CALLABLE_TASK_TYPE",
  178: "CALLBACK_TASK_TYPE",
  179: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  180: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  181: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  182: "FIXED_ARRAY_TYPE",
  183: "BOILERPLATE_DESCRIPTION_TYPE",
  184: "DESCRIPTOR_ARRAY_TYPE",
  185: "HASH_TABLE_TYPE",
  186: "SCOPE_INFO_TYPE",
  187: "TRANSITION_ARRAY_TYPE",
  188: "CELL_TYPE",
  189: "CODE_DATA_CONTAINER_TYPE",
  190: "FEEDBACK_CELL_TYPE",
  191: "FEEDBACK_VECTOR_TYPE",
  192: "LOAD_HANDLER_TYPE",
  193: "PROPERTY_ARRAY_TYPE",
  194: "PROPERTY_CELL_TYPE",
  195: "SHARED_FUNCTION_INFO_TYPE",
  196: "SMALL_ORDERED_HASH_MAP_TYPE",
  197: "SMALL_ORDERED_HASH_SET_TYPE",
  198: "STORE_HANDLER_TYPE",
  199: "WEAK_CELL_TYPE",
  200: "WEAK_FIXED_ARRAY_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1064: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1065: "JS_DATE_TYPE",
  1066: "JS_ERROR_TYPE",
  1067: "JS_GENERATOR_OBJECT_TYPE",
  1068: "JS_MAP_TYPE",
  1069: "JS_MAP_KEY_ITERATOR_TYPE",
  1070: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1071: "JS_MAP_VALUE_ITERATOR_TYPE",
  1072: "JS_MESSAGE_OBJECT_TYPE",
  1073: "JS_PROMISE_TYPE",
  1074: "JS_REGEXP_TYPE",
  1075: "JS_SET_TYPE",
  1076: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1077: "JS_SET_VALUE_ITERATOR_TYPE",
  1078: "JS_STRING_ITERATOR_TYPE",
  1079: "JS_WEAK_MAP_TYPE",
  1080: "JS_WEAK_SET_TYPE",
  1081: "JS_TYPED_ARRAY_TYPE",
  1082: "JS_DATA_VIEW_TYPE",
  1083: "WASM_INSTANCE_TYPE",
  1084: "WASM_MEMORY_TYPE",
  1085: "WASM_MODULE_TYPE",
  1086: "WASM_TABLE_TYPE",
  1087: "JS_BOUND_FUNCTION_TYPE",
  1088: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  0x02201: (138, "FreeSpaceMap"),
  0x02259: (132, "MetaMap"),
  0x022b1: (131, "NullMap"),
  0x02309: (184, "DescriptorArrayMap"),
  0x02361: (182, "FixedArrayMap"),
  0x023b9: (152, "OnePointerFillerMap"),
  0x02411: (152, "TwoPointerFillerMap"),
  0x02469: (131, "UninitializedMap"),
  0x024c1: (8, "OneByteInternalizedStringMap"),
  0x02519: (131, "UndefinedMap"),
  0x02571: (129, "HeapNumberMap"),
  0x025c9: (131, "TheHoleMap"),
  0x02621: (131, "BooleanMap"),
  0x02679: (136, "ByteArrayMap"),
  0x026d1: (182, "FixedCOWArrayMap"),
  0x02729: (185, "HashTableMap"),
  0x02781: (128, "SymbolMap"),
  0x027d9: (72, "OneByteStringMap"),
  0x02831: (186, "ScopeInfoMap"),
  0x02889: (195, "SharedFunctionInfoMap"),
  0x028e1: (133, "CodeMap"),
  0x02939: (182, "FunctionContextMap"),
  0x02991: (188, "CellMap"),
  0x029e9: (199, "WeakCellMap"),
  0x02a41: (194, "GlobalPropertyCellMap"),
  0x02a99: (135, "ForeignMap"),
  0x02af1: (187, "TransitionArrayMap"),
  0x02b49: (191, "FeedbackVectorMap"),
  0x02ba1: (131, "ArgumentsMarkerMap"),
  0x02bf9: (131, "ExceptionMap"),
  0x02c51: (131, "TerminationExceptionMap"),
  0x02ca9: (131, "OptimizedOutMap"),
  0x02d01: (131, "StaleRegisterMap"),
  0x02d59: (182, "NativeContextMap"),
  0x02db1: (182, "ModuleContextMap"),
  0x02e09: (182, "EvalContextMap"),
  0x02e61: (182, "ScriptContextMap"),
  0x02eb9: (182, "BlockContextMap"),
  0x02f11: (182, "CatchContextMap"),
  0x02f69: (182, "WithContextMap"),
  0x02fc1: (182, "DebugEvaluateContextMap"),
  0x03019: (182, "ScriptContextTableMap"),
  0x03071: (151, "FeedbackMetadataArrayMap"),
  0x030c9: (182, "ArrayListMap"),
  0x03121: (130, "BigIntMap"),
  0x03179: (183, "BoilerplateDescriptionMap"),
  0x031d1: (137, "BytecodeArrayMap"),
  0x03229: (189, "CodeDataContainerMap"),
  0x03281: (1057, "ExternalMap"),
  0x032d9: (150, "FixedDoubleArrayMap"),
  0x03331: (185, "GlobalDictionaryMap"),
  0x03389: (190, "ManyClosuresCellMap"),
  0x033e1: (1072, "JSMessageObjectMap"),
  0x03439: (182, "ModuleInfoMap"),
  0x03491: (134, "MutableHeapNumberMap"),
  0x034e9: (185, "NameDictionaryMap"),
  0x03541: (190, "NoClosuresCellMap"),
  0x03599: (185, "NumberDictionaryMap"),
  0x035f1: (190, "OneClosureCellMap"),
  0x03649: (185, "OrderedHashMapMap"),
  0x036a1: (185, "OrderedHashSetMap"),
  0x036f9: (193, "PropertyArrayMap"),
  0x03751: (185, "SimpleNumberDictionaryMap"),
  0x037a9: (182, "SloppyArgumentsElementsMap"),
  0x03801: (196, "SmallOrderedHashMapMap"),
  0x03859: (197, "SmallOrderedHashSetMap"),
  0x038b1: (185, "StringTableMap"),
  0x03909: (200, "WeakFixedArrayMap"),
  0x03961: (185, "WeakHashTableMap"),
  0x039b9: (106, "NativeSourceStringMap"),
  0x03a11: (64, "StringMap"),
  0x03a69: (73, "ConsOneByteStringMap"),
  0x03ac1: (65, "ConsStringMap"),
  0x03b19: (77, "ThinOneByteStringMap"),
  0x03b71: (69, "ThinStringMap"),
  0x03bc9: (67, "SlicedStringMap"),
  0x03c21: (75, "SlicedOneByteStringMap"),
  0x03c79: (66, "ExternalStringMap"),
  0x03cd1: (82, "ExternalStringWithOneByteDataMap"),
  0x03d29: (74, "ExternalOneByteStringMap"),
  0x03d81: (98, "ShortExternalStringMap"),
  0x03dd9: (114, "ShortExternalStringWithOneByteDataMap"),
  0x03e31: (0, "InternalizedStringMap"),
  0x03e89: (2, "ExternalInternalizedStringMap"),
  0x03ee1: (18, "ExternalInternalizedStringWithOneByteDataMap"),
  0x03f39: (10, "ExternalOneByteInternalizedStringMap"),
  0x03f91: (34, "ShortExternalInternalizedStringMap"),
  0x03fe9: (50, "ShortExternalInternalizedStringWithOneByteDataMap"),
  0x04041: (42, "ShortExternalOneByteInternalizedStringMap"),
  0x04099: (106, "ShortExternalOneByteStringMap"),
  0x040f1: (140, "FixedUint8ArrayMap"),
  0x04149: (139, "FixedInt8ArrayMap"),
  0x041a1: (142, "FixedUint16ArrayMap"),
  0x041f9: (141, "FixedInt16ArrayMap"),
  0x04251: (144, "FixedUint32ArrayMap"),
  0x042a9: (143, "FixedInt32ArrayMap"),
  0x04301: (145, "FixedFloat32ArrayMap"),
  0x04359: (146, "FixedFloat64ArrayMap"),
  0x043b1: (147, "FixedUint8ClampedArrayMap"),
  0x04409: (149, "FixedBigUint64ArrayMap"),
  0x04461: (148, "FixedBigInt64ArrayMap"),
  0x044b9: (172, "Tuple2Map"),
  0x04511: (170, "ScriptMap"),
  0x04569: (163, "InterceptorInfoMap"),
  0x045c1: (154, "AccessorInfoMap"),
  0x04619: (153, "AccessCheckInfoMap"),
  0x04671: (155, "AccessorPairMap"),
  0x046c9: (156, "AliasedArgumentsEntryMap"),
  0x04721: (157, "AllocationMementoMap"),
  0x04779: (158, "AllocationSiteMap"),
  0x047d1: (159, "AsyncGeneratorRequestMap"),
  0x04829: (160, "ContextExtensionMap"),
  0x04881: (161, "DebugInfoMap"),
  0x048d9: (162, "FunctionTemplateInfoMap"),
  0x04931: (164, "ModuleInfoEntryMap"),
  0x04989: (165, "ModuleMap"),
  0x049e1: (166, "ObjectTemplateInfoMap"),
  0x04a39: (167, "PromiseCapabilityMap"),
  0x04a91: (168, "PromiseReactionMap"),
  0x04ae9: (169, "PrototypeInfoMap"),
  0x04b41: (171, "StackFrameInfoMap"),
  0x04b99: (173, "Tuple3Map"),
  0x04bf1: (174, "WasmCompiledModuleMap"),
  0x04c49: (175, "WasmDebugInfoMap"),
  0x04ca1: (176, "WasmSharedModuleDataMap"),
  0x04cf9: (177, "CallableTaskMap"),
  0x04d51: (178, "CallbackTaskMap"),
  0x04da9: (179, "PromiseFulfillReactionJobTaskMap"),
  0x04e01: (180, "PromiseRejectReactionJobTaskMap"),
  0x04e59: (181, "PromiseResolveThenableJobTaskMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("OLD_SPACE", 0x02201): "NullValue",
  ("OLD_SPACE", 0x02231): "EmptyDescriptorArray",
  ("OLD_SPACE", 0x02251): "EmptyFixedArray",
  ("OLD_SPACE", 0x02261): "UninitializedValue",
  ("OLD_SPACE", 0x022e1): "UndefinedValue",
  ("OLD_SPACE", 0x02311): "NanValue",
  ("OLD_SPACE", 0x02321): "TheHoleValue",
  ("OLD_SPACE", 0x02371): "HoleNanValue",
  ("OLD_SPACE", 0x02381): "TrueValue",
  ("OLD_SPACE", 0x023f1): "FalseValue",
  ("OLD_SPACE", 0x02441): "empty_string",
  ("OLD_SPACE", 0x02459): "EmptyScopeInfo",
  ("OLD_SPACE", 0x02469): "ArgumentsMarker",
  ("OLD_SPACE", 0x024c1): "Exception",
  ("OLD_SPACE", 0x02519): "TerminationException",
  ("OLD_SPACE", 0x02579): "OptimizedOut",
  ("OLD_SPACE", 0x025d1): "StaleRegister",
  ("OLD_SPACE", 0x02661): "EmptyByteArray",
  ("OLD_SPACE", 0x02681): "EmptyFixedUint8Array",
  ("OLD_SPACE", 0x026a1): "EmptyFixedInt8Array",
  ("OLD_SPACE", 0x026c1): "EmptyFixedUint16Array",
  ("OLD_SPACE", 0x026e1): "EmptyFixedInt16Array",
  ("OLD_SPACE", 0x02701): "EmptyFixedUint32Array",
  ("OLD_SPACE", 0x02721): "EmptyFixedInt32Array",
  ("OLD_SPACE", 0x02741): "EmptyFixedFloat32Array",
  ("OLD_SPACE", 0x02761): "EmptyFixedFloat64Array",
  ("OLD_SPACE", 0x02781): "EmptyFixedUint8ClampedArray",
  ("OLD_SPACE", 0x027e1): "EmptyScript",
  ("OLD_SPACE", 0x02879): "ManyClosuresCell",
  ("OLD_SPACE", 0x02889): "EmptySloppyArgumentsElements",
  ("OLD_SPACE", 0x028a9): "EmptySlowElementDictionary",
  ("OLD_SPACE", 0x028f1): "EmptyOrderedHashMap",
  ("OLD_SPACE", 0x02919): "EmptyOrderedHashSet",
  ("OLD_SPACE", 0x02951): "EmptyPropertyCell",
  ("OLD_SPACE", 0x02979): "EmptyWeakCell",
  ("OLD_SPACE", 0x029e9): "NoElementsProtector",
  ("OLD_SPACE", 0x02a11): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x02a21): "SpeciesProtector",
  ("OLD_SPACE", 0x02a49): "StringLengthProtector",
  ("OLD_SPACE", 0x02a59): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x02a81): "ArrayBufferNeuteringProtector",
  ("OLD_SPACE", 0x02b09): "InfinityValue",
  ("OLD_SPACE", 0x02b19): "MinusZeroValue",
  ("OLD_SPACE", 0x02b29): "MinusInfinityValue",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "WASM_TO_WASM",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.