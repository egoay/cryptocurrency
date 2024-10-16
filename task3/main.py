from utils import Stack
from utils import transaction

def locking_script(stack:Stack,tx:transaction)->bool:
    sig,pubK=tx.parse_script_sig()
    pubK_Hash=tx.parse_script_pubkey()
    stack.push(sig)
    stack.push(pubK)
    stack.dup()
    stack.hash160()
    stack.push(pubK_Hash)
    e=stack.equl_verify()
    if e==True:
        print("hash matched")
    else:
        print("hash not match")
    return stack.check_sig(tx)

def main():
    hex_string_tx="0100000001186f9f998a5aa6f048e51dd8419a14d8a0f1a8a2836dd734d2804fe65fa35779000000008b483045022100884d142d86652a3f47ba4746ec719bbfbd040a570b1deccbb6498c75c4ae24cb02204b9f039ff08df09cbe9f6addac960298cad530a863ea8f53982c09db8f6e381301410484ecc0d46f1918b30928fa0e4ed99f16a0fb4fde0735e7ade8416ab9fe423cc5412336376789d172787ec3457eee41c04f4938de5cc17b4a10fa336a8d752adfffffffff0260e31600000000001976a914ab68025513c3dbd2f7b92a94e0581f5d50f654e788acd0ef8000000000001976a9147f9b1a7fb68d60c536c2fd8aeaa53a8f3cc025a888ac00000000"
    tx=transaction(hex_string_tx)
    stack=Stack()
    result=locking_script(stack,tx)
    
    print(result)

if __name__ == "__main__":
    main()
    