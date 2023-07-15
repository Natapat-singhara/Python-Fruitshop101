fruit = {'apple':150,'durian':300,'orange':50, 'bannana':22}

menucheck = {'a':'apple','b':'durian','c':'orange','d':'bannana'}


print('ยินดีต้อนรับเข้าสู่โปรแกรมขายสินค้า')
print('------')
mainmenu = '''
ยินดีต้อนรับเข้าสู่โปรแกรมคำนวณ
[1] -สินค้าหลายชิ้น
[2] -สินค้าชิ้นเดียว
[3] -ปิดโปรแกรม
'''



while True:
    print(mainmenu)
    menu = input('กรุณาเลือกเมนู [1]-[3]: ')
    text1 = '''
    --------------------
    ***ขายสินค้าหลายชิ้น***
    --------------------
    '''
    text2 = '''
    --------------------
    ###ขายสินค้าชิ้นเดียว###
    --------------------
    '''
    allproduct = []
    productcheck = []
    submenu1 = ''
    submenu2 = 'input_submenu2'

    if menu == '1':
        print(text1)
        while submenu1.lower() != 'q':
            print('กรุณาเลือกสินค้า\n[A]-apple [B]-durian [C]-orange [D]-bannana หรือกด [T] Summary [Q] Exit menu')
            submenu1 = input('สินค้า: ')
            if submenu1.lower() != 'q' and submenu1.lower() != 't':
                product = menucheck[submenu1.lower()]
                price = fruit[product]
                qty = float(input('จำนวน (kg): '))
                #ttl = price * qty
                d = [product , qty]
                if product not in productcheck:
                    productcheck.append(product)
                    allproduct.append(d)
                else:
                    product_index = productcheck.index(product) #ตรวจสอบว่าสินค้าที่เคยเพิ่มแล้วอยู่ตรง index ไหน
                    #allproduct[product_index][1] + จำนวน[qty] #ex.a[i][1] = a[i][1] + 3
                    allproduct[product_index][1] = allproduct[product_index][1] + qty
                    
            elif submenu1.lower() == 'q':
                print('[Q] กำลังออกจากเมนู...')
                break
            elif submenu1.lower() == 't':
                print('[T] กำลังรวมยอด...')
                grand_ttl = 0
                for name,sum_price in allproduct:
                    cal = fruit[name] * sum_price
                    print('-{} จำนวน: {} กิโลกรัม (รวม {:,.2f} บาท)'.format(name,sum_price,cal))
                    grand_ttl = grand_ttl + cal #grand_total += cal
                print('ยอดรวมทั้งหมด: {:,.2f} บาท'.format(grand_ttl))
                print('----------')
                break
            print('----------')
    elif menu == '2':
        product = input('กรุณาเลือกสินค้า: apple | durian | orange | bannana: ')
        quantity = float(input('จำนวนสินค้า กี่กิโลกรัม: '))
        cal2 = quantity * fruit[product]
        print('-{} จำนวน: {} กิโลกรัม (รวม {:,.2f} บาท)'.format(product,quantity,cal2))
        print('----------')
        break
    elif menu == '3':
        break
    
    elif menu != '1' and '2':
        print('wrong pleas shoot new one')
        break
            
    #print(allproduct)
            