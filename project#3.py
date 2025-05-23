
def geomatric_sums_calculations (factor_a, common_ratio):
#calling print function in elements variable for use in fstrings
elements = printing_of_elements(common_ratio, factor_a)
#calculations below
if common_ratio < 1:
sum_infinite_convergence = ((factor_a) / (1 - common_ratio))
print(f"This Geometric Progression does converge to a fintie number
{sum_infinite_convergence}")
print(f"The first few elements are {elements}")
elif common_ratio >= 1:
number_of_elements = int(input("This Geometric Progression does no converge
to a infintie elements. Please enter the number of elements: "))
sum_of_all_elements = factor_a * ((common_ratio ** number_of_elements) - 1)
/ (common_ratio - 1)
print(f"This Geometric Progression with {number_of_elements} is equal to
{sum_of_all_elements}")
print(f"The first few elements are {elements}")
def printing_of_elements(common_ratio, factor_a):
list_of_elements = []
for i in range(3):
element = factor_a * (common_ratio ** i)
list_of_elements.append(element)
return list_of_elements
#program input and output below
factor_a = float(input("Please enter a factor: "))
common_ratio = float(input("Please enter a ratio: "))
print("")
geomatric_sums_calculations(factor_a, common_ratio)
print("")
