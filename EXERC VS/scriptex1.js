
function calculaidade(idade_digitada, ano_atual){
    resultado = ano_atual - idade_digitada
    return resultado
}

let nome = prompt("digite o seu nome: ")
let idade = parseInt(prompt("digite a sua idade: "))
let atual = parseInt(prompt("digite o ano: "))

anonasc = calculaidade( idade, atual )

document.getElementById("anonascimento").innerHTML = "seu ano de nascimento é " + anonasc

let = numero prompt("digite um numero: ")
