def longestCommonPrefix(strs):
        output_str = ""
        length = [len(x) for x in strs]
        min_length = min(length)
        i = 0
        while i < min_length:
            for j in range(len(strs)):
                if strs[0][i]==strs[j][i]:
                    letter = True
                else:
                    letter = False
                    break
            if letter:
                output_str += strs[0][i]
                i += 1
            else:
                break
        return output_str

inp = ["c","acc","ccc"]
out = longestCommonPrefix(inp)
print(out)
