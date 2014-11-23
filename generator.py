import string
import inspect
import random
from random import choice

#helper functions
def depth_ok():
	return len(inspect.stack()) <= 20

def ID():
	return ''.join(random.choice(string.ascii_lowercase) for _ in range(3))

def Num():
	return str(random.randint(1, 100))

#generator
def Program():
	return DeclarationList()

def DeclarationList():
	base = ""
	for i in range(random.randint(0, 5)):
		base += Declaration()
	return base	

def Declaration():
	branch = random.randint(1, 2)
	if branch == 1:
		return VarDeclaration()
	else:
		return FunDeclaration()	

def VarDeclaration():
	branch = random.randint(1, 2)
	if branch == 1:
		return TypeSpecifier() + ID() + ";\n"
	else:
		return TypeSpecifier() + ID() + "[" + Num() + "];\n"

def TypeSpecifier():
	branch = random.randint(1, 2)
	if branch == 1:
		return "int "
	else:
		return "void "	

def FunDeclaration():
	return TypeSpecifier() + ID() + "(" + Params() + ")" + CompoundStmt()

def Params():
	branch = random.randint(1, 2)
	if branch == 1:
		return ParamList()
	else:
		return "void"

def ParamList():
	base = Param()
	for i in range(random.randint(0, 5)):
		base += ", " + Param()
	return base	

def Param():
	branch = random.randint(1, 2)
	if branch == 1:
		return TypeSpecifier() + ID()
	else:
		return TypeSpecifier() + ID() + "[]"

def CompoundStmt():
	return "{\n" + LocalDeclarations() + "\n" + StatementList() + "}\n"

def LocalDeclarations():
	base =""
	for i in range(random.randint(0, 5)):
		base += VarDeclaration()
	return base		

def StatementList():
	base =""
	for i in range(random.randint(0, 5)):
		base += Statement()
	return base			

def Statement():
	branch = random.randint(1, 5)
	if depth_ok and branch == 1:
		return ExpressionStmt()
	elif depth_ok and branch == 2: 
		return CompoundStmt()		

	elif depth_ok and branch == 3:
		return SelectionStmt()

	elif depth_ok and branch == 4:
		return IterationStmt()	

	else:
		return ReturnStmt()

def ExpressionStmt():
	branch = random.randint(1, 2)
	if branch == 1:
		#fix
		return Expression() + ";\n"
	else:
		return ";\n"	

def SelectionStmt():
	branch = random.randint(1, 2)
	if branch == 1:
		#fix
		return "if ( " + Expression() + ") " + Statement()
	else:
		return "if ( " + Expression() + ") " + Statement() + " else " + Statement()

def IterationStmt():
	return "while( " + Expression() + " ) " + Statement()

def ReturnStmt():
	branch = random.randint(1, 2)
	if depth_ok and branch == 1:
		return "return " + Expression() + ";\n"
	else:
		return "return;"

def Expression():
	branch = random.randint(1, 2)
	if depth_ok and branch == 1:
		return Var() + " = " + Expression()
	else:
		return SimpleExpression()

def Var():
	branch = random.randint(1, 2)
	if depth_ok and branch == 1:
		return ID() + "[" + Expression() + "]"
	else:
		return ID()

def SimpleExpression():
	branch = random.randint(1, 2)
	if depth_ok and branch == 1:
		return AdditiveExpression() + " " + Relop() + " " + AdditiveExpression()
	else:
		return AdditiveExpression()

def AdditiveExpression():
	base = Term()
	for i in range(random.randint(0, 5)):
		base += Addop() + Term()
	return base			

def Term():
	base = Factor()
	for i in range(random.randint(0, 5)):
		base += Mulop() + Factor()
	return base	

def Factor():
	branch = random.randint(1, 4)
	if depth_ok and branch == 1:
		return "(" + Expression() + ")"
	elif depth_ok and branch == 2:
		return Var()
	elif depth_ok and branch == 3:
		return Call()
	else:
		return Num()

def Call():
	return ID() + "(" + Args() + ")"

def Args():
	branch = random.randint(1, 2)
	if depth_ok and branch == 1:
		return ArgList()
	elif branch == 2:
		return ""

def ArgList():
	base = Expression()
	for i in range(random.randint(0, 5)):
		base += ", " + Expression()
	return base		

def Relop():
	return choice(["<=", "<", ">", ">=", "==", "!="])

def Addop():
	return choice(["+", "-"])

def Mulop():
	return choice(["*", "/"])

if __name__ == '__main__':
	print Program()