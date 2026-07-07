message = "###&&&Hello, World!&&&###"
print(message)
print(message.removeprefix("###&&&"))
print(message.removesuffix("&&&###"))
print(message.removeprefix("###&&&").removesuffix("&&&###"))
