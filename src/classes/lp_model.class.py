"""
Linear Programming Model Class
"""
from ..helpers import file_data_parser

class LPModel:

    m_obj_type: int
    m_devars_vector: list[type(float)]
    m_cost_vector: list[type(float)]
    m_coef_matrix: list[list[type(float)]]
    m_resource_vector: list[type(float)]
    m_vars_domain: list[type(int)]
    m_slackvars_vector: list[type(float)]

    def get_slack_variables():
        self
        a

    def __init__(self, t_obj_type, t_vars_vector, t_cost_vector, t_coef_matrix, t_resource_vector, t_vars_domain):
        self.m_obj_type = t_obj_type
        self.m_vars_vector = t_vars_vector
        self.m_cost_vector = t_cost_vector
        self.m_coef_matrix = t_coef_matrix
        self.m_resource_vector = t_resource_vector
        self.m_vars_domain = t_vars_domain
        self.m_slackvars_vector = 
