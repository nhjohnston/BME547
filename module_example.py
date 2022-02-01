import blood_calculator as bc
print("This is the database module and python calls it {}".format(__name__))
# importing a single function
# now you can just use the name of the function (without the . format)
# if there are multiple modules with the same name of a function,
# python will run the most recently imported one
# import both packages to use the . format
# to reference which function you want,
# use an alias to refer to the package


HDL_value = 55

classification = bc.check_HDL(HDL_value)

print("55 is {}".format(classification))

x = bc.check_LDL(200)
print("200 is {}".format(x))
