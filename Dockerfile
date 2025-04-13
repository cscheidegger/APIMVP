
# Estágio de construção (build)
FROM node:18-alpine AS build

# Definir o diretório de trabalho
WORKDIR /app

# Copiar package.json e package-lock.json
COPY package*.json ./

# Instalar dependências
RUN npm ci

# Copiar todos os arquivos do projeto
COPY . .

# Construir o aplicativo para produção
RUN npm run build

# Estágio de produção
FROM nginx:alpine

# Copiar os arquivos de build para o nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Copiar configuração personalizada do nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expor a porta 80
EXPOSE 80

# Comando para iniciar o nginx
CMD ["nginx", "-g", "daemon off;"]
