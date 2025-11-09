# Configuración de Odoo para AMANÓN E.I.R.L.

**Fecha de inicio:** 09/11/2025
**Versión de Odoo:** 19.0
**Empresa:** AMANÓN E.I.R.L.
**RUC:** 20611230673

---

## 📋 ÍNDICE
1. [Datos de la Empresa](#datos-de-la-empresa)
2. [Usuarios del Sistema](#usuarios-del-sistema)
3. [Clientes y Proveedores](#clientes-y-proveedores)
4. [Productos y Catálogo](#productos-y-catálogo)
5. [Impuestos y Configuración Fiscal](#impuestos-y-configuración-fiscal)
6. [Módulos Instalados](#módulos-instalados)
7. [Configuraciones Pendientes](#configuraciones-pendientes)
8. [Facturación Electrónica](#facturación-electrónica)

---

## ✅ 1. DATOS DE LA EMPRESA

### Información Básica
- [x] **Razón Social:** AMANÓN E.I.R.L.
- [x] **RUC:** 20611230673
- [x] **Dirección:** AV. SAN JUAN DE VILCA ASC. LAS DALIAS MZA. D LOTE. 4
- [x] **Distrito:** Puente Piedra
- [x] **Ciudad:** Lima
- [x] **Departamento:** Lima
- [x] **País:** Perú

### Información de Contacto
- [x] **Teléfono:** 51 903 204 089
- [x] **Email:** amanonn.pe@gmail.com
- [x] **WhatsApp:** +51 903 204 089
- [ ] **Website:** (pendiente)
- [ ] **Logo de la empresa:** (pendiente)

---

## ✅ 2. USUARIOS DEL SISTEMA

### Usuarios Configurados
- [x] **Nayiby Alejandra Borrero Arias**
  - Email/Login: nayibyborrero@gmail.com
  - Contraseña: adminAmanonErp2025
  - Rol: Administrador total
  - Estado: Activo

### Usuarios del Sistema (No modificar)
- [x] admin (usuario original - pendiente desactivar/renombrar)
- [x] OdooBot (sistema)
- [x] Public user (sistema)

### Pendientes
- [ ] Crear usuarios adicionales si se necesitan
- [ ] Desactivar o renombrar usuario "admin" original
- [ ] Configurar permisos específicos por usuario si es necesario

---

## ✅ 3. CLIENTES Y PROVEEDORES

### Clientes (13 clientes - 19 registros totales)
- [x] Rosa Elena Atoche - Lima (ID: 7)
- [x] Edelmiro Waldo Miguel Villar - Andahuaylas (ID: 8)
- [x] Érika Rodríguez Martínez - Trujillo (ID: 9)
- [x] Brenda Angélica Prado Sánchez + HARD SKIN EIRL - Arequipa (ID: 10-11)
- [x] Yesenia Sánchez - Callao (ID: 12)
- [x] Esther Vega Cruzado + Mayra Garcia Vega - Trujillo (ID: 13-14)
- [x] Catalina + COB Productos Naturales - Miraflores (ID: 15-16)
- [x] Silvia Giovanna Ludeña Rosas - Lima (ID: 17)
- [x] Vero + Julio César Laguna García - Chosica (ID: 18-19)
- [x] Elena Cecilia Meneses Esterripa - Cañete (ID: 20)
- [x] Marianny Rodriguez + Nixer Deiner Rodríguez Ledezma - Trujillo (ID: 21-22)
- [x] Kathier Vargas Guillermo + KAIZEN INTEGRACION COMERCIAL E.I.R.L. - Trujillo (ID: 23-24)
- [x] Griselda Edith Pérez Flores - Breña (ID: 25)

**Notas:**
- Todos los clientes tienen DNI/RUC, teléfonos, direcciones y notas especiales configuradas
- Campo `customer_rank = 1` para todos los clientes
- Campo `complete_name` configurado correctamente para búsquedas

### Proveedores (5 proveedores)
- [x] José Abadía M. Importaciones SAC - Lima (ID: 26)
  - RUC: 20504363903
  - Contacto: Johanna Martínez (968 245 406)
  - Horario: L-V 8:30am-5:00pm

- [x] Quimicos Goicochea S.A.C. - Callao (ID: 27)
  - RUC: 20211040352
  - Contacto: Karol Lazo (981 347 400)

- [x] Insuquimica - Lima (ID: 28)
  - RUC: 20510921128
  - Contacto: Reyna (993 523 033)
  - Horario: L-V 8:00-12:30 y 2:00-5:00pm, Sáb 8:00-12:30

- [x] PFLUCKER E HIJOS S.A. - Lima (ID: 29)
  - RUC: 20100704065
  - Contacto: Vendedor 1 (998 377 301)
  - Horario: L-V 8:30am-1:00pm y 2:00pm-5:00pm, Sáb 8:30am-1:00pm

- [x] COCOS&NUTS SAC - Chorrillos (ID: 30)
  - RUC: 20516431432
  - Teléfono: 981 236 453
  - Horario: L-V 7:30am-6:30pm

**Notas:**
- Todos los proveedores tienen `supplier_rank = 1` y `customer_rank = 0`
- Horarios y contactos guardados en campo de comentarios

### Pendientes
- [ ] Agregar más clientes según sea necesario
- [ ] Agregar más proveedores según sea necesario
- [ ] Configurar términos de pago específicos por cliente/proveedor

---

## ✅ 4. PRODUCTOS Y CATÁLOGO

### Categorías Creadas (12 categorías)
- [x] Bases para Jabones (ID: 9)
- [x] Ceras Vegetales (ID: 10)
- [x] Fragancias (ID: 11)
- [x] Aceites Esenciales (ID: 12)
- [x] Aditivos para Velas (ID: 13)
- [x] Moldes (ID: 14)
- [x] Moldes Navidad (ID: 15)
- [x] Colorantes (ID: 16)
- [x] Parafinas (ID: 17)
- [x] Moldes para Velas (ID: 18)
- [x] Polvos Micronutrientes (ID: 19)
- [x] Mechas para Velas (ID: 20)

### Productos (41 productos reales + 2 del sistema)
- [x] **Productos cargados vía CSV:** 41 productos
- [x] **Productos demo desactivados:** 42 productos demo eliminados
- [x] **Productos del sistema activos:** Tips, Down Payment (POS)

### Resumen de Productos por Categoría

#### Bases para Jabones (6 productos)
- Base de Glicerina Cristal - S/ 25.50
- Base de Glicerina Ámbar - S/ 25.00
- Base de Glicerina Blanca - S/ 25.00
- Base de Glicerina Premium de Coco - S/ 26.00
- Base de Glicerina Premium de Oliva - S/ 26.00
- Base de Glicerina Premium de Carbón Activado - S/ 26.00

#### Ceras Vegetales (3 productos)
- Cera de Soya 1kg - S/ 40.00
- Cera de Coco - S/ 48.00
- Cera de Soya AFP - S/ 48.00

#### Fragancias (2 productos)
- Fragancias 50 mL - S/ 20.00
- Fragancias 10mL - S/ 6.00

#### Aceites Esenciales (3 productos)
- Aceite esencial Árbol de Té 15 mL - S/ 22.00
- Aceite Esencial Ylang Ylang 15 mL - S/ 20.00
- Aceite Esencial de Naranja 15 mL - S/ 16.00

#### Aditivos para Velas (3 productos)
- Ácido esteárico 1 Kg - S/ 16.00
- Cera Carnauba 100 gr - S/ 10.00
- Cera Alba 100 gr - S/ 12.00

#### Otros
- Moldes (3 productos)
- Moldes Navidad (3 productos)
- Colorantes (3 productos)
- Parafinas (3 productos)
- Moldes para Velas (3 productos)
- Polvos Micronutrientes (6 productos)
- Mechas para Velas (3 productos)

### Pendientes
- [ ] Configurar imágenes de productos
- [ ] Configurar códigos de barras/SKU si es necesario
- [ ] Configurar costos de compra de productos
- [ ] Configurar stock mínimo y máximo por producto
- [ ] Configurar variantes de producto si aplica (ej: diferentes tamaños)

---

## ✅ 5. IMPUESTOS Y CONFIGURACIÓN FISCAL

### Impuestos Configurados
- [x] **IGV 18% (Ventas)** - ID: 1
  - Tipo: Venta
  - Porcentaje: 18.00%
  - Nombre: IGV 18%
  - Estado: Activo

- [x] **IGV 18% (Compras)** - ID: 2
  - Tipo: Compra
  - Porcentaje: 18.00%
  - Nombre: IGV 18%
  - Estado: Activo

- [x] **0% Exports** - ID: 3 (Exportaciones)
- [x] **0% Imports** - ID: 4 (Importaciones)

### Configuración de Empresa
- [x] **Impuesto de venta predeterminado:** IGV 18% (ID: 1)
- [x] **Impuesto de compra predeterminado:** IGV 18% (ID: 2)

### Términos de Pago Disponibles
- [x] Pago inmediato
- [x] 15 días
- [x] 21 días
- [x] 30 días
- [x] 45 días
- [x] Fin del siguiente mes
- [x] 30% ahora, resto en 60 días
- [x] Otros términos estándar

### Pendientes
- [ ] Configurar percepciones si aplica
- [ ] Configurar retenciones si aplica
- [ ] Configurar impuestos específicos adicionales si es necesario

---

## ✅ 6. MÓDULOS INSTALADOS

### Módulos Base
- [x] **account** - Contabilidad
- [x] **sale** - Ventas
- [x] **sale_management** - Gestión de ventas
- [x] **purchase** - Compras
- [x] **stock** - Inventario
- [x] **account_edi** - Facturación electrónica (base)
- [x] **contacts** - Contactos

### Módulos de Localización Peruana
- [x] **l10n_latam_base** - Localización Latinoamérica Base (v19.0.1.0)
- [x] **l10n_latam_invoice_document** - Documentos de facturación LATAM (v19.0.1.0)
- [x] **base_address_extended** - Direcciones extendidas (v19.0.1.1)
- [x] **l10n_pe** - Localización Peruana (v19.0.3.1) ✅ **INSTALADO**
- [x] **l10n_pe_pos** - Punto de venta peruano (v19.0.1.0)

### Funcionalidades Activadas por l10n_pe
- [x] Plan contable peruano (PCGE)
- [x] Tipos de comprobantes SUNAT:
  - Factura (01)
  - Boleta (03)
  - Nota de Crédito (07)
  - Nota de Débito (08)
  - Recibo por Honorarios (02)
  - Otros comprobantes oficiales

- [x] Tipos de identificación:
  - RUC
  - DNI
  - Carnet de extranjería
  - Pasaporte
  - Otros documentos

- [x] Datos de Perú:
  - 1,872 distritos cargados
  - Bancos peruanos
  - Ciudades y departamentos

- [x] Campos peruanos en facturas y contactos

### Pendientes
- [ ] Configurar módulo de facturación electrónica completo (firma digital, envío SUNAT)
- [ ] Instalar módulo de reportes adicionales si es necesario
- [ ] Configurar módulo de CRM si se requiere
- [ ] Configurar módulo de eCommerce si se requiere

---

## ⚠️ 7. CONFIGURACIONES PENDIENTES

### Métodos de Pago
- [x] Efectivo Amanon (configurado)
- [ ] Cuenta bancaria específica (nombre del banco, número de cuenta, CCI)
- [ ] Yape (número)
- [ ] Plin
- [ ] Tarjeta de crédito/débito
- [ ] Otros métodos de pago

### Diarios Contables
- [x] Ventas (INV) - Configurado
- [x] Compras (BILL) - Configurado
- [x] Banco genérico - Configurado
- [x] Efectivo Amanon - Configurado
- [ ] Configurar diarios específicos por método de pago
- [ ] Configurar series de comprobantes en diarios

### Series de Comprobantes
Actualmente tiene en uso: **E001-XXX** (según factura de ejemplo)

Pendiente configurar:
- [ ] Serie de Facturas: E001 o F001
- [ ] Serie de Boletas: B001
- [ ] Serie de Notas de Crédito: EC01 o FC01
- [ ] Serie de Notas de Débito: ED01 o FD01
- [ ] Serie de Guías de Remisión (si aplica)

### Almacenes e Inventario
- [ ] Configurar almacenes físicos
- [ ] Configurar ubicaciones de almacenamiento
- [ ] Configurar rutas de envío
- [ ] Configurar métodos de valoración de inventario (FIFO, Promedio, etc.)
- [ ] Hacer inventario inicial de stock

### Configuración de Ventas
- [ ] Configurar plantillas de cotización
- [ ] Configurar reglas de precio (descuentos, promociones)
- [ ] Configurar política de devoluciones
- [ ] Configurar términos y condiciones de venta
- [ ] Configurar correos automáticos de confirmación

### Configuración de Compras
- [ ] Configurar reglas de reabastecimiento automático
- [ ] Configurar límites de aprobación de compras
- [ ] Configurar correos automáticos a proveedores

### Reportes y Análisis
- [ ] Configurar reportes personalizados si es necesario
- [ ] Configurar dashboard de ventas
- [ ] Configurar KPIs importantes

---

## 🚨 8. FACTURACIÓN ELECTRÓNICA

### Estado Actual
- [x] **l10n_pe instalado** - Proporciona estructura básica peruana
- [x] **Tipos de comprobantes SUNAT** - Configurados en sistema
- [x] **Plan contable peruano** - Instalado

### Lo que SÍ tiene (l10n_pe básico)
- ✅ Tipos de documentos peruanos
- ✅ Numeración correlativa de comprobantes
- ✅ Estructura contable peruana
- ✅ Campos necesarios para comprobantes
- ✅ Impresión de comprobantes (sin validez electrónica SUNAT)

### Lo que NO tiene (requiere configuración adicional)
- ❌ **Firma digital de XMLs** - No genera ni firma XMLs
- ❌ **Envío automático a SUNAT** - No se comunica con webservices SUNAT
- ❌ **Generación de códigos QR** - No genera QR requerido por SUNAT
- ❌ **Obtención de CDR** - No recibe Constancia de Recepción
- ❌ **Certificado digital** - No usa certificado para firmar

### Opciones para Facturación Electrónica Completa

#### OPCIÓN 1: PSE Externo (RECOMENDADO) ⭐
**Proveedor sugerido:** NUBEFACT

**Ventajas:**
- ✅ Más fácil y rápido de implementar
- ✅ Soporte técnico incluido
- ✅ Actualizaciones automáticas según cambios SUNAT
- ✅ Certificado digital incluido en algunos planes
- ✅ Menor riesgo técnico

**Costo:**
- Plan Básico: ~S/39/mes (300 comprobantes)
- Plan Profesional: ~S/99/mes (ilimitado)

**Requiere:**
- [ ] Crear cuenta en NUBEFACT (https://nubefact.com/)
- [ ] Configurar series de comprobantes en NUBEFACT
- [ ] Obtener Token API de NUBEFACT
- [ ] Crear módulo de integración Odoo-NUBEFACT (pendiente desarrollar)
- [ ] Configurar certificado digital (si no está incluido)

**Flujo de trabajo:**
1. Crear venta en Odoo
2. Confirmar venta
3. Odoo envía datos a NUBEFACT vía API
4. NUBEFACT genera XML, firma y envía a SUNAT
5. NUBEFACT devuelve PDF, XML y CDR a Odoo
6. Comprobante queda registrado en Odoo

#### OPCIÓN 2: Módulo OCA Gratuito
**Repositorios:**
- https://github.com/oca/l10n-peru
- https://github.com/odoope/odoope-server-tools

**Ventajas:**
- ✅ Gratuito (open source)
- ✅ Integración directa con Odoo

**Desventajas:**
- ⚠️ Requiere configuración técnica avanzada
- ⚠️ Puede no estar actualizado para Odoo 19
- ⚠️ Sin soporte técnico oficial
- ⚠️ Requiere contratar un OSE adicional
- ⚠️ Más complejo de mantener

**Requiere:**
- [ ] Verificar compatibilidad con Odoo 19
- [ ] Instalar módulos adicionales de OCA
- [ ] Contratar un OSE (Operador de Servicios Electrónicos)
- [ ] Configurar certificado digital
- [ ] Configurar conexión con OSE
- [ ] Pruebas exhaustivas

#### OPCIÓN 3: Módulo Comercial
**Proveedores:**
- Locperu (~$300-500/año)
- Adhoc (~$400/año)
- Odoope Premium (~$200-300/año)

**Ventajas:**
- ✅ Todo incluido y listo para usar
- ✅ Soporte técnico profesional
- ✅ Actualizaciones garantizadas
- ✅ Funciona directo con SUNAT o con OSE

**Desventajas:**
- ⚠️ Costo anual adicional
- ⚠️ Dependencia del proveedor

### Decisión Pendiente
- [ ] **Seleccionar opción de facturación electrónica**
- [ ] **Implementar solución elegida**
- [ ] **Configurar certificado digital**
- [ ] **Configurar series en sistema de facturación**
- [ ] **Realizar pruebas antes de producción**

### Información Adicional
**Serie actual en uso:** E001-154 (según factura de ejemplo del 20/10/2025)

**Datos de factura de ejemplo:**
- Cliente: CORPORACION VIDA QUIMICA S.A.C.
- RUC Cliente: 20606244585
- Producto: BASE DE GLICERINA PREMIUM DE COCO
- Cantidad: 10 kg
- Precio unitario: S/ 20.33898
- Subtotal: S/ 203.39
- IGV 18%: S/ 36.61
- Total: S/ 240.00
- Forma de pago: Contado

---

## 📊 RESUMEN GENERAL

### ✅ COMPLETADO (80%)
1. ✅ Datos de la empresa
2. ✅ Usuario administrador
3. ✅ 13 clientes con datos completos
4. ✅ 5 proveedores con contactos
5. ✅ 41 productos reales en 12 categorías
6. ✅ Impuestos IGV 18% configurados
7. ✅ Módulo l10n_pe instalado
8. ✅ Tipos de comprobantes SUNAT
9. ✅ Plan contable peruano
10. ✅ Productos demo eliminados

### ⚠️ PENDIENTE (20%)
1. ⚠️ Métodos de pago específicos
2. ⚠️ Series de comprobantes en diarios
3. ⚠️ Facturación electrónica completa (firma, envío SUNAT)
4. ⚠️ Configuración de inventario inicial
5. ⚠️ Logo de la empresa
6. ⚠️ Imágenes de productos
7. ⚠️ Costos de compra de productos
8. ⚠️ Almacenes y ubicaciones

---

## 📝 NOTAS IMPORTANTES

### Base de Datos
- **Nombre BD:** odoo_database_name
- **Usuario BD:** odoo_user_name
- **Puerto:** 5432
- **Motor:** PostgreSQL 15

### Contenedores Docker
- **odoo_web:** Aplicación Odoo (puerto 8069)
- **odoo_db:** Base de datos PostgreSQL (puerto 5432)

### Accesos
- **URL:** http://168.231.116.236:8069
- **Usuario admin original:** admin (pendiente desactivar)
- **Usuario operativo:** nayibyborrero@gmail.com / adminAmanonErp2025

### Archivos de Configuración
- **docker-compose.yml:** /home/keba2503/clients/oddo-amanon/docker-compose.yml
- **odoo.conf:** /home/keba2503/clients/oddo-amanon/config/odoo.conf
- **Addons personalizados:** /home/keba2503/clients/oddo-amanon/addons/

---

## 🔄 PRÓXIMOS PASOS RECOMENDADOS

### Prioridad Alta
1. [ ] Decidir e implementar solución de facturación electrónica
2. [ ] Configurar series de comprobantes oficiales
3. [ ] Hacer inventario inicial de productos (stock actual)
4. [ ] Configurar métodos de pago reales

### Prioridad Media
5. [ ] Agregar imágenes a productos
6. [ ] Configurar costos de compra
7. [ ] Configurar almacenes
8. [ ] Hacer una venta de prueba completa

### Prioridad Baja
9. [ ] Agregar logo de empresa
10. [ ] Configurar reportes personalizados
11. [ ] Configurar correos automáticos

---

**Última actualización:** 09/11/2025
**Responsable:** Claude Code + Nayiby Borrero
**Estado general:** Sistema funcional al 80% - Listo para ventas básicas, pendiente facturación electrónica
