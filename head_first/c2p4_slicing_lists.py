# convert "Don't Panic!" to "on tap"

original_phrase = "Don't Panic!"
original_list = list(original_phrase)
print('original list',original_list)
# original list ['D', 'o', 'n', "'", 't', ' ', 'P', 'a', 'n', 'i', 'c', '!']

temp_list = original_list[1:3]+original_list[4:8]
print('temp_list',temp_list)
# temp_list ['o', 'n', 't', ' ', 'P', 'a']

temp_list.insert(2,temp_list.pop(3))
print('temp_list',temp_list)
# temp_list ['o', 'n', ' ', 't', 'P', 'a']

temp_list.extend([temp_list.pop(),temp_list.pop()])
print('temp_list',temp_list)
# temp_list ['o', 'n', ' ', 't', 'a', 'P']

final_list = temp_list.copy()
final_phrase = ''.join(final_list)
print('final phrase',final_phrase)
# final phrase on taP
