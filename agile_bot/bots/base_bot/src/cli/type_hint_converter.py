class TypeHintConverter:
    
    @staticmethod
    def to_cli_type(field_type) -> str:
        type_str = str(field_type)
        if 'Dict' in type_str:
            return 'dict'
        elif 'List' in type_str:
            return 'list'
        elif 'bool' in type_str:
            return 'flag'
        elif 'Scope' in type_str:
            return 'dict'
        return 'str'



