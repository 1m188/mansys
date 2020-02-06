cmake_minimum_required(VERSION 3.15)
project(stuinfo_c LANGUAGES C)

aux_source_directory(src sources)
file(GLOB menu_srcs src/menu/*.c)
add_executable(${PROJECT_NAME} ${sources} ${menu_srcs})

if(MSVC)
    target_compile_options(${PROJECT_NAME} PRIVATE /utf-8)
endif()