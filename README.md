Peter Kupka, Základy klaudvých technológií

Skúška

Aplikácia pozostáva z webovej python stránky a SQL databázy.
Na SQL server možno pripojiť napríklad pomocou 
SQL Server Management Studio, kde je možné upravovať databázu.
Aplikácia slúži na prevod celých čísel z desiatkovej 
sústavy do dvojkovej a šestnástkovej sústavy.

Trvalý zväzok: statefulset.yaml - Stará sa o zálohovanie dát 
v prípade, že je aplikácia ukončená alebo spadne.. Je tu definovaný objekt PersistentVolume.
Kubeernetes objekty som pridal do pomenovaného zväzku skuska.
Aplikácia je nasadená pomocou objektu deployment.
Service.yaml mi pridelí verejnú IP adresu pomocou príkazu:
kubectl get all -n skuska. 

Najprv sa zostavý obraz kontajnera, v ktorom bude uložená 
aplikácia. Obrazu sa pridelí meno: convert:dev.
Ak chcete vo verejnom klaude použiť vlastný obraz 
kontajnera tak ho musíte najprv umiestniť do dostupného
registra obrazov. Najprv sa vytvorí skupina zdrojov do ktorej
sa vytvorí register obrazu s menom: registerconvert.
Potom bolo potrebné prepojiť riadkového klienta s Azure Kubernetes klastrom.
Nakoniec sa vytvorý menný zväzok a aplikujú sa kubernetes objekty.
