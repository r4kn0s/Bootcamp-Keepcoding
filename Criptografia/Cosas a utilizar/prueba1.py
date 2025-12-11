from psec import tr31
def importar():
    kbpk_b = bytes.fromhex("A1A10101010101010101010101010103")
    kb = "D0144C0AB00S0000D67DB4180E4D545999D0874FADF8A8BE4319D062528246EF52E4FE90FA59A82E2E0813BDDAA2FF112A5B511D2E304185D8DB0ECCE4FF9110719ADDE054DFCCD8"
    MykeyBlock =tr31.KeyBlock(kbpk_b).unwrap(kb).hex()
    print("Importar Clave:" + tr31.KeyBlock(kbpk_b).unwrap(kb).hex())
    print("Exportabilidad:" + tr31.KeyBlock(MykeyBlock).header.exportability)
    print("Uso clave:" + tr31.KeyBlock(MykeyBlock).header.algorithm)
   # print("Header: "+ str(MykeyBlock.header))

def exportar():
    h = tr31.Header()
    h.version_id = "D"
    h.key_usage = "C0"
    h.algorithm = "A"
    h.mode_of_use = "B"
    h.exportability = "S"

    kbpk = bytes.fromhex("A1A10101010101010101010101010103")
    key = bytes.fromhex("A2A1c1c1c1c1c1c1c1c1c1c1c1c1c1c2")
    kb = tr31.KeyBlock(kbpk, h)
    print("Fase de Exportación: " + kb.wrap(key))


if __name__ == "__main__":
  
    importar()
    