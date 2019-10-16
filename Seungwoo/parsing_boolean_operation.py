def accumulate(lst, func):
    res = lst[0]
    for elem in lst[1:]:
        res = func(res, elem)
        
    return res 
        
def find_match(expr, idx = 0):
    assert expr[idx] == '('
    tmp = 0
    for c_idx, char in enumerate(expr[idx:]):
        if char == '(':
           tmp += 1
        elif char == ')':
            tmp -= 1 
        
        if tmp == 0:
            return c_idx + idx 
    
class Tree:
    def __init__(self, root, children = []):
        self.root = root
        self.children = children 
        
    
def eval(expr):
    if isinstance(expr, str):
        parse_tree = parse(expr)
        return eval(parse_tree)
    
    if expr.root == 't':
        return True 
    elif expr.root == 'f':
        return False 
    elif expr.root == '!':
        assert len(expr.children) == 1 
        return not eval(expr.children[0])
    elif expr.root == '|':
        return accumulate([eval(e) for e in expr.children], lambda x,y:x or y)
    elif expr.root == '&':
        return accumulate([eval(e) for e in expr.children], lambda x,y:x and y)
    else:
        assert False, 'Not expected Token %s'%expr
        
def parse(expr):
    res = []
    idx = 0
    _, tree = parse_expr(expr, idx)
    
    return tree
    
literal = ['t', 'f']
unary_operator = ['!']
nary_operator = ['&', '|']
    
def parse_expr(expr, idx):
    if expr[idx] in literal:
        return idx + 1, Tree(expr[idx])
    
    elif expr[idx] in unary_operator:
        assert expr[idx+1] == '(', 'Opening para expected'
        
        end = find_match(expr, idx+1)
        operand = expr[idx+2:find_match(expr, idx+1)]
        
        return end+1, Tree(expr[idx], [parse(operand)])
    elif expr[idx] in nary_operator:
        assert expr[idx+1] == '(', 'Opening para expected'
        
        operand = []
        cur = idx+2
        end = find_match(expr, idx+1)
        while cur < end:
            cur, tree = parse_expr(expr, cur)
            operand.append(tree) 
            # print(expr[cur:])
            cur += 1 
        return end+1, Tree(expr[idx], operand)
    else:
        assert False, expr
        
        
        
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        return eval(expression)