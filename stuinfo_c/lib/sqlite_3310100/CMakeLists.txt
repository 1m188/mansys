set(target_name sqlite3)
aux_source_directory(. sources)
add_library(${target_name} STATIC ${sources})
target_include_directories(${target_name} INTERFACE .)