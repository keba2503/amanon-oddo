# Dockerfile para Odoo con localización peruana (l10n_pe)
FROM odoo:latest

USER root

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar signxml (la única dependencia faltante para l10n_pe_edi)
# pyOpenSSL, zeep, cryptography y lxml ya están en la imagen base de Odoo
RUN pip3 install --no-cache-dir --break-system-packages --ignore-installed \
    signxml

USER odoo
