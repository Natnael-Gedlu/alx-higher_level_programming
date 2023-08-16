#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);

    /* Iterate through the list */
    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, typeName);
    }
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));
    if (size > 10)
        size = 10;
    printf("  first %zd bytes: ", size);
    for (Py_ssize_t i = 0; i < size; i++)
        printf("%02hhx%c", bytes->ob_sval[i], i < size - 1 ? ' ' : '\n');
}

int main(void)
{
    Py_Initialize();

    PyObject *list = PyList_New(0);
    PyObject *bytes = PyBytes_FromStringAndSize("Hello", 5);

    print_python_list(list);
    print_python_bytes(bytes);

    Py_DECREF(list);
    Py_DECREF(bytes);

    Py_Finalize();

    return 0;
}
