'use strict';

let basket = {
    list: [],
    costAll: 0,
    numberAll: 0,
    addProduct: function (product) {
        if (!this.basketPlus1(product)) {
            this.list.push({item: product, number: 1});
            this.costAll += product.cost;
            addBasketTableItem(product.id, product.name, product.cost);
        }
        this.numberAll += 1;
    },
    basketPlus1: function (product) {
        for (let i = 0; i < this.list.length; i++) {
            if (this.list[i].item === product) {
                this.list[i].number += 1;
                this.costAll += product.cost;
                plusBasketTableItem(product.id);
                return true;
            }
        }
        return false;
    }
};

let products = {
    items: [],
    addProduct: function (Product) {
        this.items.push(Product);
    }
};

const Product = function(id, name, cost) {
    this.id = id;
    this.name = name;
    this.cost = cost;
};


document.addEventListener('DOMContentLoaded', function () {
    let catalog = document.querySelector('.catalog');
    catalog.childNodes.forEach(node => {
        if (node.tagName === 'DIV') {
            let id = node.id;
            let name = 'undefined';
            let cost = 0;
            node.childNodes.forEach(node => {
                if ((node.tagName === 'P') && ('name'.includes(node.classList.value))) {
                    name = node.textContent;
                }
                if ((node.tagName === 'P') && ('cost'.includes(node.classList.value))) {
                    cost = Number(node.textContent);
                }
            });
            products.addProduct(new Product(id, name, cost));
        }
    });
});

document.querySelectorAll('button').forEach(node => {
    node.addEventListener('click', function () {
        for (let i = 0; i < products.items.length; i++) {
            if (products.items[i].id === this.parentNode.id) {
                basket.addProduct(products.items[i]);
                return;
            }
        }
    })
});

const addBasketTableItem = function (id, name, cost) {
    let newTR = document.createElement("tr");
    let newTD = document.createElement("td");
    let newP = document.createElement("p");
    let newText = document.createTextNode(name);
    newP.appendChild(newText);
    newTD.appendChild(newP);

    newP = document.createElement("p");
    newP.id = 'cost_' + id;
    newText = document.createTextNode('Стоимость: ' + cost);
    newP.appendChild(newText);
    newTD.appendChild(newP);

    newP = document.createElement("p");
    newP.id = 'number_' + id;
    newText = document.createTextNode('Количество: 1');
    newP.appendChild(newText);
    newTD.appendChild(newP);

    newP = document.createElement("p");
    newP.id = 'sum_cost_' + id;
    newText = document.createTextNode('Итого: ' + cost);
    newP.appendChild(newText);
    newTD.appendChild(newP);

    newTR.appendChild(newTD);
    newTR.border = '2px';
    let basket_table = document.querySelector('.basket_table');
    basket_table.appendChild(newTR);

    sumBasketTableItem(cost);
};

const plusBasketTableItem = function (id) {
    let numberTag = document.getElementById('number_' + id);
    let sumCostTag = document.getElementById('sum_cost_' + id);

    let costTagInt = Number(document.getElementById('cost_' + id).textContent.split(' ')[1]);
    let numberTagInt = Number(document.getElementById('number_' + id).textContent.split(' ')[1]);
    let sumCostTagInt = Number(document.getElementById('sum_cost_' + id).textContent.split(' ')[1]);

    numberTag.textContent = 'Количество: ' + Number(numberTagInt + 1);
    sumCostTag.textContent = 'Итого: ' + Number(sumCostTagInt + costTagInt);

    sumBasketTableItem(costTagInt);
};

const sumBasketTableItem = function (appendCost) {
    let sumBasket = document.querySelector('.sum_basket');
    sumBasket.textContent = "Итого: " + Number(Number(sumBasket.textContent.split(' ')[1]) + Number(appendCost));
}