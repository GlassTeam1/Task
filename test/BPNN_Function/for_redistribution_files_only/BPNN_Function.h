//
// MATLAB Compiler: 6.4 (R2017a)
// Date: Wed Oct 31 20:54:04 2018
// Arguments:
// "-B""macro_default""-W""cpplib:BPNN_Function""-T""link:lib""-d""H:\PythonCode
// \test\BPNN_Function\for_testing""-v""H:\PythonCode\test\BPNN_Function.m"
//

#ifndef __BPNN_Function_h
#define __BPNN_Function_h 1

#if defined(__cplusplus) && !defined(mclmcrrt_h) && defined(__linux__)
#  pragma implementation "mclmcrrt.h"
#endif
#include "mclmcrrt.h"
#include "mclcppclass.h"
#ifdef __cplusplus
extern "C" {
#endif

#if defined(__SUNPRO_CC)
/* Solaris shared libraries use __global, rather than mapfiles
 * to define the API exported from a shared library. __global is
 * only necessary when building the library -- files including
 * this header file to use the library do not need the __global
 * declaration; hence the EXPORTING_<library> logic.
 */

#ifdef EXPORTING_BPNN_Function
#define PUBLIC_BPNN_Function_C_API __global
#else
#define PUBLIC_BPNN_Function_C_API /* No import statement needed. */
#endif

#define LIB_BPNN_Function_C_API PUBLIC_BPNN_Function_C_API

#elif defined(_HPUX_SOURCE)

#ifdef EXPORTING_BPNN_Function
#define PUBLIC_BPNN_Function_C_API __declspec(dllexport)
#else
#define PUBLIC_BPNN_Function_C_API __declspec(dllimport)
#endif

#define LIB_BPNN_Function_C_API PUBLIC_BPNN_Function_C_API


#else

#define LIB_BPNN_Function_C_API

#endif

/* This symbol is defined in shared libraries. Define it here
 * (to nothing) in case this isn't a shared library. 
 */
#ifndef LIB_BPNN_Function_C_API 
#define LIB_BPNN_Function_C_API /* No special import/export declaration */
#endif

extern LIB_BPNN_Function_C_API 
bool MW_CALL_CONV BPNN_FunctionInitializeWithHandlers(
       mclOutputHandlerFcn error_handler, 
       mclOutputHandlerFcn print_handler);

extern LIB_BPNN_Function_C_API 
bool MW_CALL_CONV BPNN_FunctionInitialize(void);

extern LIB_BPNN_Function_C_API 
void MW_CALL_CONV BPNN_FunctionTerminate(void);



extern LIB_BPNN_Function_C_API 
void MW_CALL_CONV BPNN_FunctionPrintStackTrace(void);

extern LIB_BPNN_Function_C_API 
bool MW_CALL_CONV mlxBPNN_Function(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[]);


#ifdef __cplusplus
}
#endif

#ifdef __cplusplus

/* On Windows, use __declspec to control the exported API */
#if defined(_MSC_VER) || defined(__BORLANDC__)

#ifdef EXPORTING_BPNN_Function
#define PUBLIC_BPNN_Function_CPP_API __declspec(dllexport)
#else
#define PUBLIC_BPNN_Function_CPP_API __declspec(dllimport)
#endif

#define LIB_BPNN_Function_CPP_API PUBLIC_BPNN_Function_CPP_API

#else

#if !defined(LIB_BPNN_Function_CPP_API)
#if defined(LIB_BPNN_Function_C_API)
#define LIB_BPNN_Function_CPP_API LIB_BPNN_Function_C_API
#else
#define LIB_BPNN_Function_CPP_API /* empty! */ 
#endif
#endif

#endif

extern LIB_BPNN_Function_CPP_API void MW_CALL_CONV BPNN_Function(int nargout, mwArray& T, const mwArray& Load_C, const mwArray& Load_T, const mwArray& URX1_C, const mwArray& URX1_T, const mwArray& URY1_C, const mwArray& URY1_T, const mwArray& URZ1_C, const mwArray& URZ1_T, const mwArray& URX2_C, const mwArray& URX2_T, const mwArray& URY2_C, const mwArray& URY2_T, const mwArray& URZ2_C, const mwArray& URZ2_T, const mwArray& URX3_C, const mwArray& URX3_T, const mwArray& URY3_C, const mwArray& URY3_T, const mwArray& URZ3_C, const mwArray& URZ3_T, const mwArray& URX4_C, const mwArray& URX4_T, const mwArray& URY4_C, const mwArray& URY4_T, const mwArray& URZ4_C, const mwArray& URZ4_T, const mwArray& URX5_C, const mwArray& URX5_T, const mwArray& URY5_C, const mwArray& URY5_T, const mwArray& URZ5_C, const mwArray& URZ5_T, const mwArray& URX6_C, const mwArray& URX6_T, const mwArray& URY6_C, const mwArray& URY6_T, const mwArray& URZ6_C, const mwArray& URZ6_T, const mwArray& URX7_C, const mwArray& URX7_T, const mwArray& URY7_C, const mwArray& URY7_T, const mwArray& URZ7_C, const mwArray& URZ7_T, const mwArray& URX8_C, const mwArray& URX8_T, const mwArray& URY8_C, const mwArray& URY8_T, const mwArray& URZ8_C, const mwArray& URZ8_T, const mwArray& URX9_C, const mwArray& URX9_T, const mwArray& URY9_C, const mwArray& URY9_T, const mwArray& URZ9_C, const mwArray& URZ9_T, const mwArray& Frequency_1, const mwArray& Frequency_2, const mwArray& Frequency_3, const mwArray& Frequency_4);

#endif
#endif
