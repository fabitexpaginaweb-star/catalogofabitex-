import sys

filepath = r'C:\Users\Det-Pc\Desktop\catalogofabitex-\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_pattern = '  },];'

new_content = '''  },
{
    id: 88,
    name: "Cobertor Polipiel",
    cat: "Cobertores",
    shortDesc: "Elegancia y calidez en polipiel suave al tacto. Disponible en 7 colores vibrantes. Medidas: 2, 2½ y 3 plazas.",
    desc: `<div style="font-size:1rem;line-height:1.7;color:var(--gray-dark);">
      <p style="margin-bottom:0.8rem;font-size:1.1rem;color:#EF4444;font-weight:700;">❌ PRODUCTO AGOTADO — FUERA DE STOCK</p>
      <p style="margin-bottom:0.8rem;">Cobertor en <strong>polipiel premium</strong>, suave al tacto y con acabado elegante. Ideal para climas frescos.</p>
      <p style="margin-bottom:0.5rem;">📏 <strong>Medidas disponibles:</strong> 2 plazas · 2½ plazas · 3 plazas</p>
      <p style="font-size:0.9rem;color:var(--gray);margin-bottom:0.5rem;">💰 Precio por confirmar</p>
      <p style="font-size:0.9rem;color:var(--gray);">🎨 7 colores disponibles: Azul, Beige, Café, Rojo, Rosa, Turquesa, Vino.</p>
      <p style="font-size:0.9rem;color:var(--gray);margin-top:0.8rem;font-style:italic;">Contáctanos por WhatsApp para consultar reposición o alternativas similares.</p>
    </div>`,
    prices: {"2 Plazas": 0, "2 1/2 Plazas": 0, "3 Plazas": 0},
    colors: [
      {name: "Azul", hex: "#4169E1", image: "COBERTORES/COBERTOR POLIPIEL/COBERTOR POLIPIEL AZUL.jpeg"},
      {name: "Beige", hex: "#D4C4A8", image: "COBERTORES/COBERTOR POLIPIEL/COBERTOR POLIPIEL BEIGE.jpeg"},
      {name: "Café", hex: "#6B4E3D", image: "COBERTORES/COBERTOR POLIPIEL/COBERTOR POLIPIEL CAFE.jpeg"},
      {name: "Rojo", hex: "#C41E3A", image: "COBERTORES/COBERTOR POLIPIEL/COBERTOR POLIPIEL ROJO.jpeg"},
      {name: "Rosa", hex: "#E8A4B8", image: "COBERTORES/COBERTOR POLIPIEL/COBERTOR POLIPIEL ROSA.jpeg"},
      {name: "Turquesa", hex: "#40E0D0", image: "COBERTORES/COBERTOR POLIPIEL/COBERTOR POLIPIEL TURQUESA.jpeg"},
      {name: "Vino", hex: "#8B1538", image: "COBERTORES/COBERTOR POLIPIEL/COBERTOR POLIPIEL VINO.jpeg"}
    ],
    badge: "Agotado",
    emoji: "🛋️",
    isNewCollection: false
  },];'''

if old_pattern not in content:
    print('ERROR: No se encontró el patrón de cierre del array')
    sys.exit(1)

# Verificar que solo hay una ocurrencia
count = content.count(old_pattern)
if count != 1:
    print(f'ERROR: Se encontraron {count} ocurrencias del patrón, se esperaba 1')
    sys.exit(1)

new_file_content = content.replace(old_pattern, new_content, 1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_file_content)

print('OK: Producto agregado exitosamente')
print(f'Nuevo tamaño del archivo: {len(new_file_content)} caracteres')

# Verificación: buscar el nuevo producto
if 'Cobertor Polipiel' in new_file_content and 'id: 88' in new_file_content:
    print('OK: Verificación exitosa - producto encontrado en el archivo')
else:
    print('ERROR: Verificación fallida - no se encontró el nuevo producto')
    sys.exit(1)
