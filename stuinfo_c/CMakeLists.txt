cmake_minimum_required(VERSION 3.15)

project(stuinfo_c LANGUAGES C)

add_subdirectory(lib/sqlite_3310100)

# 按平台选择控制台的底层实现
if(WIN32)
    set(platform_source src/utility/console_win.c)
else()
    set(platform_source src/utility/console_posix.c)
endif()

file(GLOB_RECURSE sources src/*.c)
# 平台实现已经在上面单独选过了，从glob结果里排除掉
list(FILTER sources EXCLUDE REGEX "console_(win|posix)\\.c$")
list(APPEND sources ${platform_source})

add_executable(${PROJECT_NAME} ${sources})

# recurse include path
function(target_include_directories_recurse target attr root)
    if(IS_DIRECTORY ${root})
        target_include_directories(${target} ${attr} ${root})
    endif()
    file(GLOB sub_srcs RELATIVE ${root} ${root}/*)
    foreach(sub ${sub_srcs})
        if(IS_DIRECTORY ${root}/${sub})
            target_include_directories_recurse(${target} ${attr} ${root}/${sub})
        endif()
    endforeach()
endfunction()
target_include_directories_recurse(${PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src)

target_link_libraries(${PROJECT_NAME} PRIVATE sqlite3 ${CMAKE_DL_LIBS})

# 单线程程序，sqlite无需线程支持，也省去对pthread的依赖
target_compile_definitions(sqlite3 PRIVATE SQLITE_THREADSAFE=0)

# 一次性迁移工具：把旧版本的data.txt导入sqlite数据库
add_executable(txt2db tools/txt2db.c)
target_include_directories(txt2db PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/lib/sqlite_3310100)
target_link_libraries(txt2db PRIVATE sqlite3 ${CMAKE_DL_LIBS})

if(MSVC)
    target_compile_options(${PROJECT_NAME} PRIVATE /utf-8)
    target_compile_options(txt2db PRIVATE /utf-8)
endif()
