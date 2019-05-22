from data2 import *


text='''Both of (these issues) are (fixed) by postponing the evaluation of annotations. {Instead (of) compiling} code which executes [expressions in] annotations at their definition time, {the compiler} stores the annotation in a string form (equivalent to the [AST of] the) expression in question. 
'''
parens= "()[]{}"
left_parens="([{"
pairs ={')':'(', ']':'[', '}':'{'}

def parent(text):
    i,text_len =0, len(text)
    while True:
        while i < text_len and text[i] not in parens:
            i += 1
        if i >= text_len:
            return
        else:
            yield text[i],i
            i += 1

st=Sstack()
for pr,i in parent(text):
    if pr in left_parens:
        st.push((pr,i))

    elif st.is_empty() or st.pop()[0] !=pairs[pr]:
        print("没有")
        break

else:
    if st.is_empty():
        print("nice")
    else:
        e= st.pop()
        print("no")
