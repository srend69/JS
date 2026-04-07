function criarArquivo(dados){
    const livrosJSON = JSON.stringify(dados)
    const fs = require('fs');
    fs.writeFileSync("livros.json", livrosJSON);
}

//criarArquivo(livros)
let arquivo
function lerArquivo(){
    arquivo = require("./livros.json")
}
lerArquivo()

function mostrarLivros(lista){
    console.log("##### ESTOQUE DE LIVROS #####")
    lista.forEach((livro) => {
        console.log(livro.titulo + " - " + 
                    livro.autor + " Ano:" + 
                    livro.ano + " Páginas:" +
                    livro.paginas + " Preço: R$ "+
                    livro.preco.toFixed(2).replaceAll(".",","))
                    console.log("-------------------------------")
    })
}
mostrarLivros(arquivo)

let livrosFiltrados = arquivo.filter((livro) => livro.preco > 100)
console.log("===============LIVROS FILTRADOS==============")
mostrarLivros(livrosFiltrados)

let livrosDesconto = arquivo.map((livro) => {
    return {...livro, preco: livro.preco * 0.9}
})
console.log("===============LIVROS COM DESCONTO==============")
mostrarLivros(livrosDesconto)
