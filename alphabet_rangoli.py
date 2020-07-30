# pass the function a integer and a pattern of letters from the alphabet would be printed out!

# example with size 10
#        ------------------j------------------
#        ----------------j-i-j----------------
#        --------------j-i-h-i-j--------------
#        ------------j-i-h-g-h-i-j------------
#        ----------j-i-h-g-f-g-h-i-j----------
#        --------j-i-h-g-f-e-f-g-h-i-j--------
#        ------j-i-h-g-f-e-d-e-f-g-h-i-j------
#        ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#        --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#        j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
#        --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#        ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#        ------j-i-h-g-f-e-d-e-f-g-h-i-j------
#        --------j-i-h-g-f-e-f-g-h-i-j--------
#        ----------j-i-h-g-f-g-h-i-j----------
#        ------------j-i-h-g-h-i-j------------
#        --------------j-i-h-i-j--------------
#        ----------------j-i-j----------------
#        ------------------j------------------

def print_rangoli(n):
    l = []
    for i in range(n):
        s= '-'.join('abcdefghijklmnopqrstuvwxyz'[i:n])
        l.append((s[::-1]+s[1:]).center(4*n-3, '-'))
    print('\n'.join(l[:0:-1]+l))
