str1="""Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""

def wordsuccesor(str1):
    word_bag={}
    Words=[]
    sentences=str1.split(".")
    for sentence in sentences:
        temp=sentence.split(",")
        for micro_sentence in temp:
            x=micro_sentence.strip()
            Words.extend(x.split(" "))
    for i in range(len(Words)):
        temp=Words[i]
        if temp not in word_bag and i!=len(Words)-1:
            word_bag[temp]=[]
            word_bag[temp].append(Words[i+1])
        if temp in word_bag and i!=len(Words)-1:
            if Words[i+1] not in word_bag[temp]:
                word_bag[temp].append(Words[i+1])
    return word_bag

x=wordsuccesor(str1)
print(x)
print(x["Python"])
