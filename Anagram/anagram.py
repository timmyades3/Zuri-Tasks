def anagram():
  str1 = "race"
  str2 = "care"

  if(len(str1) == len(str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)


    if(sorted_str1 == sorted_str2):
      print(" find_Anagrams " + "(" + str1 + " and " + str2 + ")" + " -->  true ")
    else:
      print("find_Anagrams" + "(" + str1 + " and " + str2 + ")"+ "-->  false ")
  else:
    print(" find_Anagrams" + "(" + str1 + " and " + str2 + ")" + "-->  false ")
anagram()          