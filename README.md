# FIAP Enterprise Connection - CPTM

## Descrição

O Enterprise Connection consiste em uma conexão entre o meio acadêmico e mercado de trabalho, em que a colaboração é estabelecida no sentido de fomentar o desenvolvimento de skills essenciais para o ingresso (ou consolidação) de profissionais de Sistemas de Informação.

Para que essa conexão aconteça, reunimos empresas e profissionais de referência para apresentarem seus cases e/ou seus microproblemas, almejando alguma solução viável e inovadora, propiciada por esta conexão.

As soluções desenvolvidas compõem as atividades (AD) de algumas disciplinas e são desenvolvidas em períodos específicos ao longo do ano. Todas as atividades de Enterprise Connection são realizadas em grupos de 3 (três) a 5 (cinco) pessoas, formados em cada conexão estabelecida.

A apresentação da empresa, com todas as informações necessárias para o desenvolvimento da atividade, acontece em uma Live, e a entrega da solução é via plataforma, como submissão de atividade

## Problema

    Acolher os trens que circularam durante o período comercial para limpeza e manutenção e a saída 
    dos trens de manutenção para os reparos noturnos 

## Dados geráis

    Quantidade de saídas para atender as manutenções programadas por pátios: 
    Lapa - 4 veículos 
    Altino - 2 veículos 
    Calmon Viana - 3 veículos

## Informações Complementares

### 1. Quais os tipos de veículos e suas atividades de manutenção?

    1.1 Máquinas de correção geométrica e/ou máquinas especiais: 
        a) Socadora de via corrida (SAP) e AMV (SCP);
        b) Reguladora de lastro (RLP);
        c) Esmerilhadora de trilhos (ETS); 
        d) Desguarnecedora de lastro (DAL) e vagões hopper (VHP); 
        e) Carro Controle (CCP). 

    1.2 Caminhão de linha (GN ou CL) 

### 2. Quais os pátios que os veículos acessam as vias?

    Linhas 7/10 = Lapa, Francisco Morato, São Caetano. 
    Linhas 8/9 = Presidente Altino. 
    Linhas 11/12 = Calmon Viana. 

### 3. Qual a distribuição dos veículos na Linhas e suas equipes?

    Os veículos descritos no item 1.1 atendem todas as Linhas da CPTM
    As equipes de caminhões de linha item 1.2 são fixas em cada par de Linhas (exceto quando atendidos 
    pela equipe DOVF Operação Plasser/Speno). 

### 4. Quais os tempos de manobras de cada veículo para atendimento dos serviços em diversas Linhas?

    O tempo de acesso do pátio para o acesso ás vias principais vai depender da quantidade de veículos em 
    cada pátio, do horário em que cada um solicita ao CCO, do tráfego momentâneo na via principal, etc. 
    De qualquer maneira não há estatísticas sobre o tema, o que se pode afirmar é que veículos compostos por 
    um único corpo não realizam manobras, já os do tipo caminhão de linha e desguarnecedora podem realizar 
    manobras tanto em pátios como em via principal.

### 5. Qual o tempo médio de atuação nas SAs de cada veículo?

    Em média são de 02 horas – mas, tal tempo depende muito da demanda programada e do tipo de 
    serviço, não há uma estatística efetiva que represente todas as situações. 

### 6. Como é comunicação com CCO (Centro de Controle da Operação)?

    Por padrão com sistema de rádio digital instalado na cabine de cada veículo (alguns que dispõem de 
    mais de uma cabine de condução devem ter o rádio instalado em ambas e funcionando em paralelo). 
    Em casos excepcionais utiliza-se de telefonia fixa ou celular (chamadas de serviço podem ser a cobrar). 

### 7. Como é o relacionamento dos veículos de via com os trens de carga?

    A prioridade de tráfego é estabelecida por PO ou conforme orientação do CCO conforme situação 
    operacional momentânea. 
    Nos pátios da MRS ou outras operadoras de carga o tráfego tem de ser combinado com o empregado 
    destas responsável pelo pátio

### Esboço do algoritmo

    Horário de manutenção: 01:00 AM a 03:30 AM.

### Estratégia principal

1. Utilizar de vias temporárias para facilitar a manobra de tréns nos pátios, começar a recolher os tréns a partir da 00:00 AM, liberar os veículos de manutenção apenás após as 01:00 AM.

2. Para calcular quando um trêm deve voltar devemos estabelecer que ele deve ter 0 passageiros após as 00:00 AM.

3. Desenvolver um algorítimo que simula minutos com base em segundos, para deixar o algorítimo mais real.

4. Calcular tempo médio de retorno de ponta A a ponto B para aplicar estrátégias de recolhimento, assim evitando que um trêm não retorne a tempo antes do horário comercial.

5. Criar um objeto trêm com própriedades como:

- Nome
- Pátio
- Pátio atual (pode ser nulo)
- Estação atual (pode ser nulo)
- Horário de manutenção
