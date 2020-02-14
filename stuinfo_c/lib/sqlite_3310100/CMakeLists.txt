set(target_name sqlite3)
aux_source_directory(. sources)
add_library(${target_name} STATIC ${sources}) # 这里只能够编译为静态库，要编译为动态库需要另外一套配置
target_include_directories(${target_name} INTERFACE .)