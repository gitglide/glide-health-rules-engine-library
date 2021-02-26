
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTleftBWORleftBWXORleftBWANDrightQMARKCOLONnonassocEQNEEQ_FZMEQ_FZSNE_FZMNE_FZSGEGTLELTINleftADDSUBleftBWLSHBWRSHleftMULTDIVFDIVMODleftPOWrightUMINUSleftATTRADD AND ATTR BWAND BWLSH BWOR BWRSH BWXOR COLON COMMA DATETIME EQ EQ_FZM EQ_FZS FALSE FDIV FLOAT FLOAT_INF FLOAT_NAN GE GT IN LBRACKET LE LPAREN LT MOD MUL NE NE_FZM NE_FZS NOT NULL OR POW QMARK RBRACKET RPAREN STRING SUB SYMBOL TDIV TRUEstatement : expression\n\t\tobject : object ATTR SYMBOL\n\t\t\n\t\texpression : object\n\t\t\n\t\texpression : expression QMARK expression COLON expression\n\t\t\n\t\texpression : expression ADD    expression\n\t\t\t\t   | expression SUB    expression\n\t\t\t\t   | expression MOD    expression\n\t\t\t\t   | expression MUL    expression\n\t\t\t\t   | expression FDIV   expression\n\t\t\t\t   | expression TDIV   expression\n\t\t\t\t   | expression POW    expression\n\t\t\n\t\texpression : expression BWAND  expression\n\t\t\t\t   | expression BWOR   expression\n\t\t\t\t   | expression BWXOR  expression\n\t\t\t\t   | expression BWLSH  expression\n\t\t\t\t   | expression BWRSH  expression\n\t\t\n\t\texpression : expression IN     expression\n\t\t\t\t   | expression NOT IN expression\n\t\t\n\t\texpression : expression EQ     expression\n\t\t\t\t   | expression NE     expression\n\t\t\n\t\texpression : expression GT     expression\n\t\t\t\t   | expression GE     expression\n\t\t\t\t   | expression LT     expression\n\t\t\t\t   | expression LE     expression\n\t\t\n\t\texpression : expression EQ_FZM expression\n\t\t\t\t   | expression EQ_FZS expression\n\t\t\t\t   | expression NE_FZM expression\n\t\t\t\t   | expression NE_FZS expression\n\t\t\n\t\texpression : expression AND    expression\n\t\t\t\t   | expression OR     expression\n\t\tobject : LPAREN expression RPARENexpression : NOT expressionobject : SYMBOLexpression : SUB expression %prec UMINUS\n\t\texpression : TRUE\n\t\t\t\t   | FALSE\n\t\tobject : DATETIMEexpression : FLOATexpression : FLOAT_NANexpression : FLOAT_INFexpression : NULLobject : STRING\n\t\tobject : LBRACKET RBRACKET\n\t\t\t   | LBRACKET members RBRACKET\n\t\t\t   | LBRACKET members COMMA RBRACKET\n\t\t\n\t\tmembers : expression\n\t\t\t\t| members COMMA expression\n\t\t\n\t\tobject : object LBRACKET expression RBRACKET\n\t\t\n\t\tobject : object LBRACKET COLON RBRACKET\n\t\t       | object LBRACKET COLON expression RBRACKET\n\t\t       | object LBRACKET expression COLON RBRACKET\n\t\t       | object LBRACKET expression COLON expression RBRACKET\n\t\t'
    
_lr_action_items = {'NOT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,],[5,31,-3,5,5,-35,-36,-38,-39,-40,-41,-33,5,-37,-42,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-34,31,31,-43,31,31,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,5,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,31,31,-2,31,5,-31,-44,5,5,-18,-48,5,-49,31,-45,31,-4,31,-51,-50,-52,]),'SUB':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,],[4,19,-3,4,4,-35,-36,-38,-39,-40,-41,-33,4,-37,-42,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,-34,19,19,-43,19,19,-5,-6,-7,-8,-9,-10,-11,19,19,19,-15,-16,19,4,19,19,19,19,19,19,19,19,19,19,19,19,-2,19,4,-31,-44,4,4,19,-48,4,-49,19,-45,19,19,19,-51,-50,-52,]),'TRUE':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'FALSE':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'FLOAT':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'FLOAT_NAN':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'FLOAT_INF':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'NULL':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'LPAREN':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'SYMBOL':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,66,81,84,85,88,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,79,12,12,12,12,12,12,]),'DATETIME':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'STRING':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'LBRACKET':([0,3,4,5,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,49,66,79,81,82,83,84,85,87,88,89,91,95,96,97,],[16,45,16,16,-33,16,-37,-42,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-43,16,-2,16,-31,-44,16,16,-48,16,-49,-45,-51,-50,-52,]),'$end':([1,2,3,6,7,8,9,10,11,12,14,15,46,47,49,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,82,83,86,87,89,91,93,95,96,97,],[0,-1,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,-32,-43,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-2,-31,-44,-18,-48,-49,-45,-4,-51,-50,-52,]),'QMARK':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[17,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,17,17,-43,17,17,-5,-6,-7,-8,-9,-10,-11,17,17,17,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,17,17,-2,17,-31,-44,-18,-48,-49,17,-45,17,17,17,-51,-50,-52,]),'ADD':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[18,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,18,18,-43,18,18,-5,-6,-7,-8,-9,-10,-11,18,18,18,-15,-16,18,18,18,18,18,18,18,18,18,18,18,18,18,-2,18,-31,-44,18,-48,-49,18,-45,18,18,18,-51,-50,-52,]),'MOD':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[20,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,20,20,-43,20,20,20,20,-7,-8,-9,-10,-11,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-2,20,-31,-44,20,-48,-49,20,-45,20,20,20,-51,-50,-52,]),'MUL':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[21,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,21,21,-43,21,21,21,21,-7,-8,-9,-10,-11,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-2,21,-31,-44,21,-48,-49,21,-45,21,21,21,-51,-50,-52,]),'FDIV':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[22,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,22,22,-43,22,22,22,22,-7,-8,-9,-10,-11,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-2,22,-31,-44,22,-48,-49,22,-45,22,22,22,-51,-50,-52,]),'TDIV':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[23,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,23,23,-43,23,23,23,23,-7,-8,-9,-10,-11,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-2,23,-31,-44,23,-48,-49,23,-45,23,23,23,-51,-50,-52,]),'POW':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[24,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,24,24,-43,24,24,24,24,24,24,24,24,-11,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-2,24,-31,-44,24,-48,-49,24,-45,24,24,24,-51,-50,-52,]),'BWAND':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[25,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,25,25,-43,25,25,-5,-6,-7,-8,-9,-10,-11,-12,25,25,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,25,25,-2,25,-31,-44,-18,-48,-49,25,-45,25,-4,25,-51,-50,-52,]),'BWOR':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[26,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,26,26,-43,26,26,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,26,26,-2,26,-31,-44,-18,-48,-49,26,-45,26,-4,26,-51,-50,-52,]),'BWXOR':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[27,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,27,27,-43,27,27,-5,-6,-7,-8,-9,-10,-11,-12,27,-14,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,27,27,-2,27,-31,-44,-18,-48,-49,27,-45,27,-4,27,-51,-50,-52,]),'BWLSH':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[28,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,28,28,-43,28,28,28,28,-7,-8,-9,-10,-11,28,28,28,-15,-16,28,28,28,28,28,28,28,28,28,28,28,28,28,-2,28,-31,-44,28,-48,-49,28,-45,28,28,28,-51,-50,-52,]),'BWRSH':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[29,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,29,29,-43,29,29,29,29,-7,-8,-9,-10,-11,29,29,29,-15,-16,29,29,29,29,29,29,29,29,29,29,29,29,29,-2,29,-31,-44,29,-48,-49,29,-45,29,29,29,-51,-50,-52,]),'IN':([2,3,6,7,8,9,10,11,12,14,15,31,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[30,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,66,-34,30,30,-43,30,30,-5,-6,-7,-8,-9,-10,-11,30,30,30,-15,-16,None,None,None,None,None,None,None,None,None,None,None,30,30,-2,30,-31,-44,None,-48,-49,30,-45,30,30,30,-51,-50,-52,]),'EQ':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[32,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,32,32,-43,32,32,-5,-6,-7,-8,-9,-10,-11,32,32,32,-15,-16,None,None,None,None,None,None,None,None,None,None,None,32,32,-2,32,-31,-44,None,-48,-49,32,-45,32,32,32,-51,-50,-52,]),'NE':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[33,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,33,33,-43,33,33,-5,-6,-7,-8,-9,-10,-11,33,33,33,-15,-16,None,None,None,None,None,None,None,None,None,None,None,33,33,-2,33,-31,-44,None,-48,-49,33,-45,33,33,33,-51,-50,-52,]),'GT':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[34,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,34,34,-43,34,34,-5,-6,-7,-8,-9,-10,-11,34,34,34,-15,-16,None,None,None,None,None,None,None,None,None,None,None,34,34,-2,34,-31,-44,None,-48,-49,34,-45,34,34,34,-51,-50,-52,]),'GE':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[35,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,35,35,-43,35,35,-5,-6,-7,-8,-9,-10,-11,35,35,35,-15,-16,None,None,None,None,None,None,None,None,None,None,None,35,35,-2,35,-31,-44,None,-48,-49,35,-45,35,35,35,-51,-50,-52,]),'LT':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[36,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,36,36,-43,36,36,-5,-6,-7,-8,-9,-10,-11,36,36,36,-15,-16,None,None,None,None,None,None,None,None,None,None,None,36,36,-2,36,-31,-44,None,-48,-49,36,-45,36,36,36,-51,-50,-52,]),'LE':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[37,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,37,37,-43,37,37,-5,-6,-7,-8,-9,-10,-11,37,37,37,-15,-16,None,None,None,None,None,None,None,None,None,None,None,37,37,-2,37,-31,-44,None,-48,-49,37,-45,37,37,37,-51,-50,-52,]),'EQ_FZM':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[38,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,38,38,-43,38,38,-5,-6,-7,-8,-9,-10,-11,38,38,38,-15,-16,None,None,None,None,None,None,None,None,None,None,None,38,38,-2,38,-31,-44,None,-48,-49,38,-45,38,38,38,-51,-50,-52,]),'EQ_FZS':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[39,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,39,39,-43,39,39,-5,-6,-7,-8,-9,-10,-11,39,39,39,-15,-16,None,None,None,None,None,None,None,None,None,None,None,39,39,-2,39,-31,-44,None,-48,-49,39,-45,39,39,39,-51,-50,-52,]),'NE_FZM':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[40,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,40,40,-43,40,40,-5,-6,-7,-8,-9,-10,-11,40,40,40,-15,-16,None,None,None,None,None,None,None,None,None,None,None,40,40,-2,40,-31,-44,None,-48,-49,40,-45,40,40,40,-51,-50,-52,]),'NE_FZS':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[41,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,41,41,-43,41,41,-5,-6,-7,-8,-9,-10,-11,41,41,41,-15,-16,None,None,None,None,None,None,None,None,None,None,None,41,41,-2,41,-31,-44,None,-48,-49,41,-45,41,41,41,-51,-50,-52,]),'AND':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[42,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,-32,42,-43,42,42,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,42,-2,42,-31,-44,-18,-48,-49,42,-45,42,-4,42,-51,-50,-52,]),'OR':([2,3,6,7,8,9,10,11,12,14,15,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,90,91,92,93,94,95,96,97,],[43,-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,-32,43,-43,43,43,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-2,43,-31,-44,-18,-48,-49,43,-45,43,-4,43,-51,-50,-52,]),'RPAREN':([3,6,7,8,9,10,11,12,14,15,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,82,83,86,87,89,91,93,95,96,97,],[-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,-32,82,-43,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-2,-31,-44,-18,-48,-49,-45,-4,-51,-50,-52,]),'RBRACKET':([3,6,7,8,9,10,11,12,14,15,16,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,93,94,95,96,97,],[-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,49,-34,-32,-43,83,-46,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-2,87,89,-31,-44,91,-18,-48,95,-49,96,-45,-47,-4,97,-51,-50,-52,]),'COMMA':([3,6,7,8,9,10,11,12,14,15,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,82,83,86,87,89,91,92,93,95,96,97,],[-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,-34,-32,-43,84,-46,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-2,-31,-44,-18,-48,-49,-45,-47,-4,-51,-50,-52,]),'COLON':([3,6,7,8,9,10,11,12,14,15,45,46,47,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,87,89,91,93,95,96,97,],[-3,-35,-36,-38,-39,-40,-41,-33,-37,-42,81,-34,-32,-43,85,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-2,88,-31,-44,-18,-48,-49,-45,-4,-51,-50,-52,]),'ATTR':([3,12,14,15,49,79,82,83,87,89,91,95,96,97,],[44,-33,-37,-42,-43,-2,-31,-44,-48,-49,-45,-51,-50,-52,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[2,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,80,86,90,92,93,94,]),'object':([0,4,5,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,45,66,81,84,85,88,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'members':([16,],[50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',241),
  ('object -> object ATTR SYMBOL','object',3,'p_expression_getattr','parser.py',246),
  ('expression -> object','expression',1,'p_expression_object','parser.py',252),
  ('expression -> expression QMARK expression COLON expression','expression',5,'p_expression_ternary','parser.py',258),
  ('expression -> expression ADD expression','expression',3,'p_expression_arithmetic','parser.py',265),
  ('expression -> expression SUB expression','expression',3,'p_expression_arithmetic','parser.py',266),
  ('expression -> expression MOD expression','expression',3,'p_expression_arithmetic','parser.py',267),
  ('expression -> expression MUL expression','expression',3,'p_expression_arithmetic','parser.py',268),
  ('expression -> expression FDIV expression','expression',3,'p_expression_arithmetic','parser.py',269),
  ('expression -> expression TDIV expression','expression',3,'p_expression_arithmetic','parser.py',270),
  ('expression -> expression POW expression','expression',3,'p_expression_arithmetic','parser.py',271),
  ('expression -> expression BWAND expression','expression',3,'p_expression_bitwise','parser.py',279),
  ('expression -> expression BWOR expression','expression',3,'p_expression_bitwise','parser.py',280),
  ('expression -> expression BWXOR expression','expression',3,'p_expression_bitwise','parser.py',281),
  ('expression -> expression BWLSH expression','expression',3,'p_expression_bitwise','parser.py',282),
  ('expression -> expression BWRSH expression','expression',3,'p_expression_bitwise','parser.py',283),
  ('expression -> expression IN expression','expression',3,'p_expression_contains','parser.py',291),
  ('expression -> expression NOT IN expression','expression',4,'p_expression_contains','parser.py',292),
  ('expression -> expression EQ expression','expression',3,'p_expression_comparison','parser.py',304),
  ('expression -> expression NE expression','expression',3,'p_expression_comparison','parser.py',305),
  ('expression -> expression GT expression','expression',3,'p_expression_arithmetic_comparison','parser.py',313),
  ('expression -> expression GE expression','expression',3,'p_expression_arithmetic_comparison','parser.py',314),
  ('expression -> expression LT expression','expression',3,'p_expression_arithmetic_comparison','parser.py',315),
  ('expression -> expression LE expression','expression',3,'p_expression_arithmetic_comparison','parser.py',316),
  ('expression -> expression EQ_FZM expression','expression',3,'p_expression_fuzzy_comparison','parser.py',324),
  ('expression -> expression EQ_FZS expression','expression',3,'p_expression_fuzzy_comparison','parser.py',325),
  ('expression -> expression NE_FZM expression','expression',3,'p_expression_fuzzy_comparison','parser.py',326),
  ('expression -> expression NE_FZS expression','expression',3,'p_expression_fuzzy_comparison','parser.py',327),
  ('expression -> expression AND expression','expression',3,'p_expression_logic','parser.py',335),
  ('expression -> expression OR expression','expression',3,'p_expression_logic','parser.py',336),
  ('object -> LPAREN expression RPAREN','object',3,'p_expression_group','parser.py',343),
  ('expression -> NOT expression','expression',2,'p_expression_negate','parser.py',347),
  ('object -> SYMBOL','object',1,'p_expression_symbol','parser.py',351),
  ('expression -> SUB expression','expression',2,'p_expression_uminus','parser.py',360),
  ('expression -> TRUE','expression',1,'p_expression_boolean','parser.py',367),
  ('expression -> FALSE','expression',1,'p_expression_boolean','parser.py',368),
  ('object -> DATETIME','object',1,'p_expression_datetime','parser.py',373),
  ('expression -> FLOAT','expression',1,'p_expression_float','parser.py',377),
  ('expression -> FLOAT_NAN','expression',1,'p_expression_float_nan','parser.py',381),
  ('expression -> FLOAT_INF','expression',1,'p_expression_float_inf','parser.py',385),
  ('expression -> NULL','expression',1,'p_expression_null','parser.py',389),
  ('object -> STRING','object',1,'p_expression_string','parser.py',393),
  ('object -> LBRACKET RBRACKET','object',2,'p_expression_array','parser.py',398),
  ('object -> LBRACKET members RBRACKET','object',3,'p_expression_array','parser.py',399),
  ('object -> LBRACKET members COMMA RBRACKET','object',4,'p_expression_array','parser.py',400),
  ('members -> expression','members',1,'p_expression_array_members','parser.py',409),
  ('members -> members COMMA expression','members',3,'p_expression_array_members','parser.py',410),
  ('object -> object LBRACKET expression RBRACKET','object',4,'p_expression_getitem','parser.py',422),
  ('object -> object LBRACKET COLON RBRACKET','object',4,'p_expression_getslice','parser.py',429),
  ('object -> object LBRACKET COLON expression RBRACKET','object',5,'p_expression_getslice','parser.py',430),
  ('object -> object LBRACKET expression COLON RBRACKET','object',5,'p_expression_getslice','parser.py',431),
  ('object -> object LBRACKET expression COLON expression RBRACKET','object',6,'p_expression_getslice','parser.py',432),
]