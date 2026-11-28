---
name: trocar-arquivo-hotmart
description: Troca o PDF de entrega de um produto (principal ou bump) na Hotmart depois que o material mudou e foi aprovado de novo. Publica o arquivo num link temporário e devolve UMA frase para o dono colar na extensão do Chrome. Use quando um PDF aprovado precisar substituir o que está na Hotmart.
---
A API da Hotmart não troca arquivo de produto; a troca é feita pela extensão do Chrome no computador do dono.

1. **Trava:** `python3 ferramentas/conferir_material.py ofertas/<pasta>` → "MATERIAL APROVADO". Sem isso, pare
   (nada sobe para a Hotmart antes do Portão M).
2. Descubra o produto: ID na Hotmart em `ofertas/<pasta>/hotmart/kit-cadastro.md` ou `campanha.md`
   (Dez Minutinhos: principal 9077469; bumps 9077648, 9085785, 9085823, 9085850, 9085887, 9085924, 9085959).
3. Publique o arquivo num link temporário com nome difícil de adivinhar:
   `publicado/<slug>/entrega-<8 letras aleatórias>/<arquivo>.pdf` (ou o `.zip`, se o produto entrega zip),
   commit + push no `main`, e espere o link responder 200 (`curl -sfI`).
4. Devolva ao dono **uma frase por produto**, pronta para a extensão:
   > Na Hotmart, no produto <nome> (<ID>), troque o arquivo de entrega pelo arquivo deste link: <URL>.
   > Baixe o arquivo, substitua o antigo, salve e me diga se o produto continua com "Vendas ativas". Não mude mais nada.
   Vários produtos: uma frase por produto, enviadas uma de cada vez (a extensão trunca prompts longos).
5. Depois que o dono confirmar: **apague** a pasta `publicado/<slug>/entrega-*/` (commit + push), registre no
   `status.md` (data, produto, hash do arquivo) e confira, se der, o download em "Minhas compras".
