"""
Input reader in LP format, as the example bellow:

objective:
(min|max) c1 * x1 + c2 * x2
subject to:
a11 * x1 + a12 * x2 = b1
domain:
x1 >= 0
x2 >= 0
"""

#from ..classes import LPModel

def read_file(t_file_path="./examples/ex1.txt"):
    data_dict = {}
    dict_key = None

    with open(t_file_path, "r") as m_file:
        for line in m_file.readlines():
            if line.endswith(":\n"):
                dict_key = line.strip()
                print(dict_key)
            else:
                if dict_key in data_dict:
                    data_dict[dict_key] += [line.strip()]
                else:
                    data_dict[dict_key] = [line.strip()]
    return data_dict
