//
// MATLAB Compiler: 6.4 (R2017a)
// Date: Wed Oct 31 20:54:04 2018
// Arguments:
// "-B""macro_default""-W""cpplib:BPNN_Function""-T""link:lib""-d""H:\PythonCode
// \test\BPNN_Function\for_testing""-v""H:\PythonCode\test\BPNN_Function.m"
//

#include <stdio.h>
#define EXPORTING_BPNN_Function 1
#include "BPNN_Function.h"

static HMCRINSTANCE _mcr_inst = NULL;


#if defined( _MSC_VER) || defined(__BORLANDC__) || defined(__WATCOMC__) || defined(__LCC__) || defined(__MINGW64__)
#ifdef __LCC__
#undef EXTERN_C
#endif
#include <windows.h>

static char path_to_dll[_MAX_PATH];

BOOL WINAPI DllMain(HINSTANCE hInstance, DWORD dwReason, void *pv)
{
    if (dwReason == DLL_PROCESS_ATTACH)
    {
        if (GetModuleFileName(hInstance, path_to_dll, _MAX_PATH) == 0)
            return FALSE;
    }
    else if (dwReason == DLL_PROCESS_DETACH)
    {
    }
    return TRUE;
}
#endif
#ifdef __cplusplus
extern "C" {
#endif

static int mclDefaultPrintHandler(const char *s)
{
  return mclWrite(1 /* stdout */, s, sizeof(char)*strlen(s));
}

#ifdef __cplusplus
} /* End extern "C" block */
#endif

#ifdef __cplusplus
extern "C" {
#endif

static int mclDefaultErrorHandler(const char *s)
{
  int written = 0;
  size_t len = 0;
  len = strlen(s);
  written = mclWrite(2 /* stderr */, s, sizeof(char)*len);
  if (len > 0 && s[ len-1 ] != '\n')
    written += mclWrite(2 /* stderr */, "\n", sizeof(char));
  return written;
}

#ifdef __cplusplus
} /* End extern "C" block */
#endif

/* This symbol is defined in shared libraries. Define it here
 * (to nothing) in case this isn't a shared library. 
 */
#ifndef LIB_BPNN_Function_C_API
#define LIB_BPNN_Function_C_API /* No special import/export declaration */
#endif

LIB_BPNN_Function_C_API 
bool MW_CALL_CONV BPNN_FunctionInitializeWithHandlers(
    mclOutputHandlerFcn error_handler,
    mclOutputHandlerFcn print_handler)
{
    int bResult = 0;
  if (_mcr_inst != NULL)
    return true;
  if (!mclmcrInitialize())
    return false;
  if (!GetModuleFileName(GetModuleHandle("BPNN_Function"), path_to_dll, _MAX_PATH))
    return false;
    {
        mclCtfStream ctfStream = 
            mclGetEmbeddedCtfStream(path_to_dll);
        if (ctfStream) {
            bResult = mclInitializeComponentInstanceEmbedded(   &_mcr_inst,
                                                                error_handler, 
                                                                print_handler,
                                                                ctfStream);
            mclDestroyStream(ctfStream);
        } else {
            bResult = 0;
        }
    }  
    if (!bResult)
    return false;
  return true;
}

LIB_BPNN_Function_C_API 
bool MW_CALL_CONV BPNN_FunctionInitialize(void)
{
  return BPNN_FunctionInitializeWithHandlers(mclDefaultErrorHandler, 
                                             mclDefaultPrintHandler);
}

LIB_BPNN_Function_C_API 
void MW_CALL_CONV BPNN_FunctionTerminate(void)
{
  if (_mcr_inst != NULL)
    mclTerminateInstance(&_mcr_inst);
}

LIB_BPNN_Function_C_API 
void MW_CALL_CONV BPNN_FunctionPrintStackTrace(void) 
{
  char** stackTrace;
  int stackDepth = mclGetStackTrace(&stackTrace);
  int i;
  for(i=0; i<stackDepth; i++)
  {
    mclWrite(2 /* stderr */, stackTrace[i], sizeof(char)*strlen(stackTrace[i]));
    mclWrite(2 /* stderr */, "\n", sizeof(char)*strlen("\n"));
  }
  mclFreeStackTrace(&stackTrace, stackDepth);
}


LIB_BPNN_Function_C_API 
bool MW_CALL_CONV mlxBPNN_Function(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[])
{
  return mclFeval(_mcr_inst, "BPNN_Function", nlhs, plhs, nrhs, prhs);
}

LIB_BPNN_Function_CPP_API 
void MW_CALL_CONV BPNN_Function(int nargout, mwArray& T, const mwArray& Load_C, const 
                                mwArray& Load_T, const mwArray& URX1_C, const mwArray& 
                                URX1_T, const mwArray& URY1_C, const mwArray& URY1_T, 
                                const mwArray& URZ1_C, const mwArray& URZ1_T, const 
                                mwArray& URX2_C, const mwArray& URX2_T, const mwArray& 
                                URY2_C, const mwArray& URY2_T, const mwArray& URZ2_C, 
                                const mwArray& URZ2_T, const mwArray& URX3_C, const 
                                mwArray& URX3_T, const mwArray& URY3_C, const mwArray& 
                                URY3_T, const mwArray& URZ3_C, const mwArray& URZ3_T, 
                                const mwArray& URX4_C, const mwArray& URX4_T, const 
                                mwArray& URY4_C, const mwArray& URY4_T, const mwArray& 
                                URZ4_C, const mwArray& URZ4_T, const mwArray& URX5_C, 
                                const mwArray& URX5_T, const mwArray& URY5_C, const 
                                mwArray& URY5_T, const mwArray& URZ5_C, const mwArray& 
                                URZ5_T, const mwArray& URX6_C, const mwArray& URX6_T, 
                                const mwArray& URY6_C, const mwArray& URY6_T, const 
                                mwArray& URZ6_C, const mwArray& URZ6_T, const mwArray& 
                                URX7_C, const mwArray& URX7_T, const mwArray& URY7_C, 
                                const mwArray& URY7_T, const mwArray& URZ7_C, const 
                                mwArray& URZ7_T, const mwArray& URX8_C, const mwArray& 
                                URX8_T, const mwArray& URY8_C, const mwArray& URY8_T, 
                                const mwArray& URZ8_C, const mwArray& URZ8_T, const 
                                mwArray& URX9_C, const mwArray& URX9_T, const mwArray& 
                                URY9_C, const mwArray& URY9_T, const mwArray& URZ9_C, 
                                const mwArray& URZ9_T, const mwArray& Frequency_1, const 
                                mwArray& Frequency_2, const mwArray& Frequency_3, const 
                                mwArray& Frequency_4)
{
  mclcppMlfFeval(_mcr_inst, "BPNN_Function", nargout, 1, 60, &T, &Load_C, &Load_T, &URX1_C, &URX1_T, &URY1_C, &URY1_T, &URZ1_C, &URZ1_T, &URX2_C, &URX2_T, &URY2_C, &URY2_T, &URZ2_C, &URZ2_T, &URX3_C, &URX3_T, &URY3_C, &URY3_T, &URZ3_C, &URZ3_T, &URX4_C, &URX4_T, &URY4_C, &URY4_T, &URZ4_C, &URZ4_T, &URX5_C, &URX5_T, &URY5_C, &URY5_T, &URZ5_C, &URZ5_T, &URX6_C, &URX6_T, &URY6_C, &URY6_T, &URZ6_C, &URZ6_T, &URX7_C, &URX7_T, &URY7_C, &URY7_T, &URZ7_C, &URZ7_T, &URX8_C, &URX8_T, &URY8_C, &URY8_T, &URZ8_C, &URZ8_T, &URX9_C, &URX9_T, &URY9_C, &URY9_T, &URZ9_C, &URZ9_T, &Frequency_1, &Frequency_2, &Frequency_3, &Frequency_4);
}

