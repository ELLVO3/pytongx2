def remove(napis, usuwany):
    return napis.replace(usuwany, "", 1)

def remove_all(napis, usuwany):
    return napis.replace(usuwany, "")

def reverse(napis):
    return napis[::-1]

def palindrom(napis):
    return napis == reverse(napis)

def mirror(napis):
    return napis + reverse(napis)

def main():
    print(remove("abrakadabra", "ab"))
    print(remove_all("abrakadabra", "ab"))
    print(reverse("hello"))
    print(palindrom("kajak"))
    print(mirror("mlem"))
main()