cmake_minimum_required(VERSION 3.15)
project(StuInfo_C)

aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR} sources)
file(GLOB_RECURSE menu_srcs ${CMAKE_CURRENT_SOURCE_DIR}/menu/*.c)
add_executable(${PROJECT_NAME} ${sources} ${menu_srcs})

if(WIN32)
    target_compile_options(${PROJECT_NAME} PRIVATE /utf-8)
endif()