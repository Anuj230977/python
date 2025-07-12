import qrcode as qr
img= qr.make("https://search.brave.com/search?q=how+to+install+a+module+in+python+in+vscode&summary=1&conversation=2042ed0d71c1964f4d864c")
img.save("module_qr.png")
#just a comment
