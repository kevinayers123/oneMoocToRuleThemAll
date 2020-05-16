import diff_match_patch as dmp_module

dmp = dmp_module.diff_match_patch()
original = open("./original.txt", "r").read()
string1 = open("./text1.txt", "r").read()
string2 = open("./text2.txt", "r").read()
patches1 = dmp.patch_make(original, string1)
print(dmp.patch_toText(patches1))
patches2 = dmp.patch_make(original, string2)
print(dmp.patch_toText(patches2))
(patch1merge, results1) = dmp.patch_apply(patches1, original)
(final, results) = dmp.patch_apply(patches2, patch1merge)
print(final)
