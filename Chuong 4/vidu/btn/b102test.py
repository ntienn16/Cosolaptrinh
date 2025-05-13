def convert_volume(units, unit_type):
  if unit_type == "cup":
    return str(units) + " cup"
  elif unit_type == "tablespoon":
    cups = units // 16 
    tablespoons = units % 16
    if cups == 0:
      return str(tablespoons) + " tablespoon"
    elif tablespoons == 0:
      return str(cups) + " cup"
    else:
      return str(cups) + " cup, " + str(tablespoons) + " tablespoon"
  elif unit_type == "teaspoon":
    cups = units // 48 # Lấy phần nguyên của phép chia cho 48
    remainder = units % 48 # Lấy phần dư của phép chia cho 48
    tablespoons = remainder // 3 # Lấy phần nguyên của phép chia cho 3
    teaspoons = remainder % 3 # Lấy phần dư của phép chia cho 3
    # Trả về chuỗi kết quả
    if cups == 0 and tablespoons == 0:
      return str(teaspoons) + " teaspoon"
    elif cups == 0 and teaspoons == 0:
      return str(tablespoons) + " tablespoon"
    elif tablespoons == 0 and teaspoons == 0:
      return str(cups) + " cup"
    elif cups == 0:
      return str(tablespoons) + " tablespoon, " + str(teaspoons) + " teaspoon"
    elif tablespoons == 0:
      return str(cups) + " cup, " + str(teaspoons) + " teaspoon"
    elif teaspoons == 0:
      return str(cups) + " cup, " + str(tablespoons) + " tablespoon"
    else:
      return str(cups) + " cup, " + str(tablespoons) + " tablespoon, " + str(teaspoons) + " teaspoon"
  
print(convert_volume(59, "teaspoon"))