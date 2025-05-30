# Charles Truscott Watters
# I love you Dad Mark William Watters
from __future__ import annotations
from queue import deque
import sys

"""
0b1
0b10
0b100
0b1000
0b10000
0b100000
0b1000000
0b10000000
0b100000000
0b1000000000
0b10000000000
0b100000000000
0b1000000000000
0b10000000000000
0b100000000000000
0b1000000000000000
0b10000000000000000
0b100000000000000000
0b1000000000000000000
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]
['L']
['L inverse']
deque([<__main__.RubiksState object at 0x7866c7e350>, <__main__.RubiksState object at 0x7866c7e490>, <__main__.RubiksState object at 0x7866c855b0>, <__main__.RubiksState object at 0x7866c84b00>, <__main__.RubiksState object at 0x7866c5f650>, <__main__.RubiksState object at 0x7866c67570>, <__main__.RubiksState object at 0x7866b61bf0>, <__main__.RubiksState object at 0x7866cb5750>, <__main__.RubiksState object at 0x7866cb5a50>, <__main__.RubiksState object at 0x7866c53200>, <__main__.RubiksState object at 0x7866c53890>, <__main__.RubiksState object at 0x7866c97cb0>])
Liszt: [(1, 1), (1, 2), (1, 4), (1, 8), (1, 16), (1, 32), (1, 64), (1, 128), (1, 256), (1, 512), (1, 1024), (1, 2048), (1, 4096), (1, 8192), (1, 16384), (1, 32768), (1, 65536), (1, 131072), (1, 262144), (2, 1), (2, 2), (2, 4), (2, 8), (2, 16), (2, 32), (2, 64), (2, 128), (2, 256), (2, 512), (2, 1024), (2, 2048), (2, 4096), (2, 8192), (2, 16384), (2, 32768), (2, 65536), (2, 131072), (2, 262144), (4, 1), (4, 2), (4, 4), (4, 8), (4, 16), (4, 32), (4, 64), (4, 128), (4, 256), (4, 512), (4, 1024), (4, 2048), (4, 4096), (4, 8192), (4, 16384), (4, 32768), (4, 65536), (4, 131072), (4, 262144), (8, 1), (8, 2), (8, 4), (8, 8), (8, 16), (8, 32), (8, 64), (8, 128), (8, 256), (8, 512), (8, 1024), (8, 2048), (8, 4096), (8, 8192), (8, 16384), (8, 32768), (8, 65536), (8, 131072), (8, 262144), (16, 1), (16, 2), (16, 4), (16, 8), (16, 16), (16, 32), (16, 64), (16, 128), (16, 256), (16, 512), (16, 1024), (16, 2048), (16, 4096), (16, 8192), (16, 16384), (16, 32768), (16, 65536), (16, 131072), (16, 262144), (32, 1), (32, 2), (32, 4), (32, 8), (32, 16), (32, 32), (32, 64), (32, 128), (32, 256), (32, 512), (32, 1024), (32, 2048), (32, 4096), (32, 8192), (32, 16384), (32, 32768), (32, 65536), (32, 131072), (32, 262144), (64, 1), (64, 2), (64, 4), (64, 8), (64, 16), (64, 32), (64, 64), (64, 128), (64, 256), (64, 512), (64, 1024), (64, 2048), (64, 4096), (64, 8192), (64, 16384), (64, 32768), (64, 65536), (64, 131072), (64, 262144), (128, 1), (128, 2), (128, 4), (128, 8), (128, 16), (128, 32), (128, 64), (128, 128), (128, 256), (128, 512), (128, 1024), (128, 2048), (128, 4096), (128, 8192), (128, 16384), (128, 32768), (128, 65536), (128, 131072), (128, 262144), (256, 1), (256, 2), (256, 4), (256, 8), (256, 16), (256, 32), (256, 64), (256, 128), (256, 256), (256, 512), (256, 1024), (256, 2048), (256, 4096), (256, 8192), (256, 16384), (256, 32768), (256, 65536), (256, 131072), (256, 262144), (512, 1), (512, 2), (512, 4), (512, 8), (512, 16), (512, 32), (512, 64), (512, 128), (512, 256), (512, 512), (512, 1024), (512, 2048), (512, 4096), (512, 8192), (512, 16384), (512, 32768), (512, 65536), (512, 131072), (512, 262144), (1024, 1), (1024, 2), (1024, 4), (1024, 8), (1024, 16), (1024, 32), (1024, 64), (1024, 128), (1024, 256), (1024, 512), (1024, 1024), (1024, 2048), (1024, 4096), (1024, 8192), (1024, 16384), (1024, 32768), (1024, 65536), (1024, 131072), (1024, 262144), (2048, 1), (2048, 2), (2048, 4), (2048, 8), (2048, 16), (2048, 32), (2048, 64), (2048, 128), (2048, 256), (2048, 512), (2048, 1024), (2048, 2048), (2048, 4096), (2048, 8192), (2048, 16384), (2048, 32768), (2048, 65536), (2048, 131072), (2048, 262144), (4096, 1), (4096, 2), (4096, 4), (4096, 8), (4096, 16), (4096, 32), (4096, 64), (4096, 128), (4096, 256), (4096, 512), (4096, 1024), (4096, 2048), (4096, 4096), (4096, 8192), (4096, 16384), (4096, 32768), (4096, 65536), (4096, 131072), (4096, 262144), (8192, 1), (8192, 2), (8192, 4), (8192, 8), (8192, 16), (8192, 32), (8192, 64), (8192, 128), (8192, 256), (8192, 512), (8192, 1024), (8192, 2048), (8192, 4096), (8192, 8192), (8192, 16384), (8192, 32768), (8192, 65536), (8192, 131072), (8192, 262144), (16384, 1), (16384, 2), (16384, 4), (16384, 8), (16384, 16), (16384, 32), (16384, 64), (16384, 128), (16384, 256), (16384, 512), (16384, 1024), (16384, 2048), (16384, 4096), (16384, 8192), (16384, 16384), (16384, 32768), (16384, 65536), (16384, 131072), (16384, 262144), (32768, 1), (32768, 2), (32768, 4), (32768, 8), (32768, 16), (32768, 32), (32768, 64), (32768, 128), (32768, 256), (32768, 512), (32768, 1024), (32768, 2048), (32768, 4096), (32768, 8192), (32768, 16384), (32768, 32768), (32768, 65536), (32768, 131072), (32768, 262144), (65536, 1), (65536, 2), (65536, 4), (65536, 8), (65536, 16), (65536, 32), (65536, 64), (65536, 128), (65536, 256), (65536, 512), (65536, 1024), (65536, 2048), (65536, 4096), (65536, 8192), (65536, 16384), (65536, 32768), (65536, 65536), (65536, 131072), (65536, 262144), (131072, 1), (131072, 2), (131072, 4), (131072, 8), (131072, 16), (131072, 32), (131072, 64), (131072, 128), (131072, 256), (131072, 512), (131072, 1024), (131072, 2048), (131072, 4096), (131072, 8192), (131072, 16384), (131072, 32768), (131072, 65536), (131072, 131072), (131072, 262144), (262144, 1), (262144, 2), (262144, 4), (262144, 8), (262144, 16), (262144, 32), (262144, 64), (262144, 128), (262144, 256), (262144, 512), (262144, 1024), (262144, 2048), (262144, 4096), (262144, 8192), (262144, 16384), (262144, 32768), (262144, 65536), (262144, 131072), (262144, 262144)]
{1: [1, 1], 2: [2, 2], 4: [4, 4], 8: [8, 8], 16: [16, 16], 32: [32, 32], 64: [64, 64], 128: [128, 128], 256: [256, 256], 512: [512, 512], 1024: [1024, 1024], 2048: [2048, 2048], 4096: [4096, 4096], 8192: [8192, 8192], 16384: [16384, 16384], 32768: [32768, 32768], 65536: [65536, 65536], 131072: [131072, 131072], 262144: [262144, 262144]}

[Program finished]
Truscott-Watters Algorithm

"""

class GraphAdjList:
    def __init__(self) -> None:
        self.adj_list: dict[any,list[any]] = {}  # Hash table of vertex to array of vertices

    def add_vertex(self, u: any) -> None:
        if u not in self.adj_list:
            self.adj_list[u] = []

    def delete_vertex(self, u: any) -> None:
        if u not in self.adj_list:
            return
        del self.adj_list[u]
        v: any
        for v in self.adj_list:
            u: any
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)

    def add_edge(self, u: any, v: any) -> None:
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def remove_edge(self, u: any, v: any) -> None:
        if u in self.adj_list and v in self.adj_list[u] and v in self.adj_list and u in self.adj_list[v]:
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)

    def edge_exists(self, u: any, v: any) -> bool:
        return u in self.adj_list and v in self.adj_list[u]

    def get_vertices(self) -> list[any]:
        return list(self.adj_list.keys())

    def get_neighbors(self, u: any) -> list[any]:
        if u not in self.adj_list:
            return []
        return self.adj_list[u]

    def initialize(self, vertices: list[any], edges: list[tuple[any,any]]) -> None:
        u: any
        for u in vertices:
            self.add_vertex(u)
        src: any; dest: any
        for src, dest in edges:
            self.add_edge(src, dest)
            
class RubiksState(object):
    def __init__(self, tlf, blf, trf, brf, tlb, blb, trb, brb, moves):
        self.tlf = tlf
        self.blf = blf
        self.trf = trf
        self.brf = brf
        self.tlb = tlb
        self.blb = blb
        self.trb = trb
        self.brb = brb
        
        self.left_face = [self.tlb[1], self.tlf[1], self.blb[1], self.blf[1]]
        self.right_face = [self.trf[1], self.trb[1], self.brf[1], self.brb[1]]
        self.front_face = [self.tlf[2], self.trf[2], self.blf[2], self.brf[2]]
        self.back_face = [self.trb[2], self.tlb[2], self.brb[2], self.blb[2]]
        self.up_face  = [self.tlb[0], self.trb[0], self.tlf[0], self.trf[0]]
        self.down_face = [self.blf[0], self.brf[0], self.blb[0], self.brb[0]]
        self.orientation = [self.front_face, self.left_face, self.right_face, self.back_face, self.up_face, self.down_face]
#        print("Front face: {}".format(self.front_face))
#        print("Left Face: {}".format(self.left_face))
#        print("Right Face: {}".format(self.right_face))
#        print("Back Face: {}".format(self.back_face))
#        print("Up face: {}".format(self.up_face))
#        print("Down face:{}".format(self.down_face))
        self.moves = moves
        if self.is_solved():
        	print("SOLVED: {}".format(self.moves))
    def L(self):
        """ TLF to TLB, TLB to BLB, BLB to BLF, BLF to TLF """
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        ntlf[0], ntlf[1], ntlf[2] = tblf[2], tblf[1], tblf[0]
        nblf[0], nblf[1], nblf[2] = tblb[2], tblb[1], tblb[0]
        ntlb[0], ntlb[1], ntlb[2] = ttlf[2], ttlf[1], ttlf[0]
        nblb[0], nblb[1], nblb[2] = ttlb[2], ttlb[1], ttlb[0]
        moves = self.moves.copy()
        moves.append('L')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def L2(self):
        """ TLF to BLB, BLB to TLF, TLB to BLF, BLF to TLB """
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        nblb[0], nblb[1], nblb[2] = ttlf[0], ttlf[1], ttlf[2]
        ntlf[0], ntlf[1], ntlf[2] = tblb[0], tblb[1], tblb[2]
        nblf[0], nblf[1], nblf[2] = ttlb[0], ttlb[1], ttlb[2]
        ntlb[0], ntlb[1], ntlb[2] = tblf[0], tblf[1], tblf[2]
        moves = self.moves.copy()
        moves.append('L2')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        return n
    def Linv(self):
        """ TLF to BLF, BLF to BLB, BLB to TLB, TLB to TLF """
        
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        nblf[0], nblf[1], nblf[2] = ttlf[2], ttlf[1], ttlf[0]
        nblb[0], nblb[1], nblb[2] = tblf[2], tblf[1], tblf[0]
        ntlb[0], ntlb[1], ntlb[2] = tblb[2], tblb[1], tblb[0]
        ntlf[0], ntlf[1], ntlf[2] = ttlb[2], ttlb[1], ttlb[0]
        moves = self.moves.copy()
        moves.append('L inverse')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
        
        pass
    def R(self):
        """ TRF to TRB, TRB to BRB, BRB to BRF, BRF to TRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ntrb[2], ntrb[1], ntrb[0] = ttrf[0], ttrf[1], ttrf[2]
        nbrb[2], nbrb[1], nbrb[0] = ttrb[0], ttrb[1], ttrb[2]
        nbrf[2], nbrf[1], nbrf[0] = tbrb[0], tbrb[1], tbrb[2]
        ntrf[2], ntrf[1], ntrf[0] = tbrf[0], tbrf[1], tbrf[2]
        moves = self.moves.copy()
        moves.append('R')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def R2(self):
        """ TRF to BRB, BRB to TRF, BRF to TRB, TRB to BRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrb[0], nbrb[1], nbrb[2] = ttrf[0], ttrf[1], ttrf[2]
        ntrf[0], ntrf[1], ntrf[2] = tbrb[0], tbrb[1], tbrb[2]
        ntrb[0], ntrb[1], ntrb[2] = tbrf[0], tbrf[1], tbrf[2]
        nbrf[0], nbrf[1], nbrf[2] = ttrb[0], ttrb[1], ttrb[2]
        moves = self.moves.copy()
        moves.append('R2')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Rinv(self):
        """ TRF to BRF, BRF to BRB, BRB to TRB, TRB to TRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrf[0], nbrf[1], nbrf[2] = ttrf[2], ttrf[1], ttrf[0]
        nbrb[0], nbrb[1], nbrb[2] = tbrf[2], tbrf[1], tbrf[0]
        ntrb[0], ntrb[1], ntrb[2] = tbrb[2], tbrb[1], tbrb[0]
        ntrf[0], ntrf[1], ntrf[2] = ttrb[2], ttrb[1], ttrb[0]
        moves = self.moves.copy()
        moves.append('R inverse')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
# From here below
    def U(self):
        """ TLF to TRF, TRF to TRB, TRB to TLB, TLB to TLF """
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntrf[0], ntrf[1], ntrf[2] = ttlf[0], ttlf[2], ttlf[1]
        ntrb[0], ntrb[1], ntrb[2] = ttrf[0], ttrf[2], ttrf[1]
        ntlb[0], ntlb[1], ntlb[2] = ttrb[0], ttrb[2], ttrb[1]
        ntlf[0], ntlf[1], ntlf[2] = ttlb[0], ttlb[2], ttlb[1]
        moves = self.moves.copy()
        moves.append('U')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    def U2(self):
        """ TLF to TRB, TRB to TLF, TRF to TLB, TLB to TRF """
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ntrb[0], ntrb[1], ntrb[2] = ttlf[0], ttlf[1], ttlf[2]
        ntlf[0], ntlf[1], ntlf[2] = ttrb[0], ttrb[1], ttrb[2]
        ntlb[0], ntlb[1], ntlb[2] = ttrf[0], ttrf[1], ttrf[2]
        ntrf[0], ntrf[1], ntrf[2] = ttlb[0], ttlb[1], ttlb[2]
        moves = self.moves.copy()
        moves.append('U2')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    def Uinv(self):
        """ TLF to TLB, TLB to TRB, TRB to TRF, TRF to TLF """
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntlb[0], ntlb[1], ntlb[2] = ttlf[0], ttlf[2], ttlf[1]
        ntrb[0], ntrb[1], ntrb[2] = ttlb[0], ttlb[2], ttlb[1]
        ntrf[0], ntrf[1], ntrf[2] = ttrb[0], ttrb[2], ttrb[1]
        ntlf[0], ntlf[1], ntlf[2] = ttrf[0], ttrf[2], ttrf[1]
        moves = self.moves.copy()
        moves.append('U inverse')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    
    def D(self):
        """ BLF to BRF, BRF to BRB, BRB to BLB, BLB to BLF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nbrf[0], nbrf[1], nbrf[2] = tblf[0], tblf[2], tblf[1]
        nbrb[0], nbrb[1], nbrb[2] = tbrf[0], tbrf[2], tbrf[1]
        nblb[0], nblb[1], nblb[2] = tbrb[0], tbrb[2], tbrb[1]
        nblf[0], nblf[1], nblf[2] = tblb[0], tblb[2], tblb[1]
        moves = self.moves.copy()
        moves.append('D')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def D2(self):
        """ BLF to BRB, BRB to BLF, BRF to BLB, BLB to BRF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nbrb[0], nbrb[1], nbrb[2] = tblf[0], tblf[1], tblf[2]
        nblf[0], nblf[1], nblf[2] = tbrb[0], tbrb[1], tbrb[2]
        nblb[0], nblb[1], nblb[2] = tbrf[0], tbrf[1], tbrf[2]
        nbrf[0], nbrf[1], nbrf[2] = tblb[0], tblb[1], tblb[2]
        moves = self.moves.copy()
        moves.append('D2')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Dinv(self):
        """ BLF to BLB, BLB to BRB, BRB to BRF, BRF to BLF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nblb[0], nblb[1], nblb[2] = tblf[0], tblf[2], tblf[1]
        nbrb[0], nbrb[1], nbrb[2] = tblb[0], tblb[2], tblb[1]
        nbrf[0], nbrf[1], nbrf[2] = tbrb[0], tbrb[2], tbrb[1]
        nblf[0], nblf[1], nblf[2] = tbrf[0], tbrf[2], tbrf[1]
        moves = self.moves.copy()
        moves.append('D inverse')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
# From here
    def F(self):
        """ TLF to BLF, BLF to BRF, BRF to TRF, TRF to TLF """
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, tblf, tbrf = self.tlf, self.trf, self.blf, self.brf
        nblf[0], nblf[1], nblf[2] = ttlf[1], ttlf[0], ttlf[2]
        nbrf[0], nbrf[1], nbrf[2] = tblf[1], tblf[0], tblf[2]
        ntrf[0], ntrf[1], ntrf[2] = tbrf[1], tbrf[0], tbrf[2]
        ntlf[0], ntlf[1], ntlf[2] = ttrf[1], ttrf[0], ttrf[2]
        moves = self.moves.copy()
        moves.append('F')
        n = RubiksState(ntlf, nblf, ntrf, nbrf, self.tlb, self.blb, self.trb, self.brb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def F2(self):
        """ TLF to BRF, BRF to TLF, TRF to BLF, BLF to TRF """
        ttlf, ttrf, tblf, tbrf = self.tlf, self.trf, self.blf, self.brf
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrf[0], nbrf[1], nbrf[2] = ttlf[0], ttlf[1], ttlf[2]
        ntlf[0], ntlf[1], ntlf[2] = tbrf[0], tbrf[1], tbrf[2]
        nblf[0], nblf[1], nblf[2] = ttrf[0], ttrf[1], ttrf[2]
        ntrf[0], ntrf[1], ntrf[2] = tblf[0], tblf[1], tblf[2]
        moves = self.moves.copy()
        moves.append('F2')
        n = RubiksState(ntlf, nblf, ntrf, nbrf, self.tlb, self.blb, self.trb, self.brb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Finv(self):
        """ TLF to TRF, TRF to BRF, BRF to BLF, BLF to TLF """
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, tblf, tbrf = self.tlf, self.trf, self.blf, self.brf
        ntrf[0], ntrf[1], ntrf[2] = ttlf[1], ttlf[0], ttlf[2]
        nbrf[0], nbrf[1], nbrf[2] = ttrf[1], ttrf[0], ttrf[2]
        nblf[0], nblf[1], nblf[2] = tbrf[1], tbrf[0], tbrf[2]
        ntlf[0], ntlf[1], ntlf[2] = tblf[1], tblf[0], tblf[2]
        moves = self.moves.copy()
        moves.append('F inverse')
        n = RubiksState(ntlf, nblf, ntrf, nbrf, self.tlb, self.blb, self.trb, self.brb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def B(self):
        """ TLB to BLB, BLB to BRB, BRB to TRB, TRB to TLB """
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlb, tblb, ttrb, tbrb = self.tlb, self.blb, self.trb, self.brb
        nblb[0], nblb[1], nblb[2] = ttlb[1], ttlb[0], ttlb[2]
        nbrb[0], nbrb[1], nbrb[2] = tblb[1], tblb[0], tblb[2]
        ntrb[0], ntrb[1], ntrb[2] = tbrb[1], tbrb[0], tbrb[2]
        ntlb[0], ntlb[1], ntlb[2] = ttrb[1], ttrb[0], ttrb[2]
        moves = self.moves.copy()
        moves.append('B')
        n = RubiksState(self.tlf, self.blf, self.trf, self.brf, ntlb, nblb, ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def B2(self):
        """ TLB to BRB, BRB to TLB, TRB to BLB, BLB to TRB """
        ttlb, tblb, ttrb, tbrb = self.tlb, self.blb, self.trb, self.brb
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrb[0], nbrb[1], nbrb[2] = ttlb[0], ttlb[1], ttlb[2]
        ntlb[0], ntlb[1], ntlb[2] = tbrb[0], tbrb[1], tbrb[2]
        nblb[0], nblb[1], nblb[2] = ttrb[0], ttrb[1], ttrb[2]
        ntrb[0], ntrb[1], ntrb[2] = tblb[0], tblb[1], tblb[2]
        moves = self.moves.copy()
        moves.append('B2')
        n = RubiksState(self.tlf, self.blf, self.trf, self.brf, ntlb, nblb, ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def Binv(self):
        """ BLB to TLB, TLB to TRB, TRB to BRB, BRB to BLB"""
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlb, tblb, ttrb, tbrb = self.tlb, self.blb, self.trb, self.brb
        ntlb[1], ntlb[0], ntlb[2] = tblb[0], tblb[1], tblb[2] 
        ntrb[1], ntrb[0], ntrb[2] = ttlb[0], ttlb[1], ttlb[2]
        nbrb[1], nbrb[0], nbrb[2] = ttrb[0], ttrb[1], ttrb[2]
        nblb[1], nblb[0], nblb[2] = tbrb[0], tbrb[1], tbrb[2]

        moves = self.moves.copy()
        moves.append("B inverse")
        n = RubiksState(self.tlf, self.blf, self.trf, self.brf, ntlb, nblb, ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def is_solved(self):
        if self.blb == ['Y', 'O', 'B'] and self.tlb == ['W', 'O', 'B'] and self.brb == ['Y', 'R', 'B'] and self.trb == ['W', 'R', 'B'] and self.blf == ['Y', 'O', 'G'] and self.tlf == ['W', 'O', 'G'] and self.brf == ['Y', 'R', 'G'] and self.trf == ['W', 'R', 'G']:
            print('Solved: {}'.format(self.moves))
            print("{}".format(self.orientation))
            exit(1)
        if self.front_face == ['G', 'G', 'G', 'G'] and self.back_face == ['B', 'B', 'B', 'B'] and self.left_face == ['O', 'O', 'O', 'O'] and self.right_face == ['R', 'R', 'R', 'R'] and self.up_face == ['W', 'W', 'W', 'W'] and self.down_face == ['Y', 'Y', 'Y', 'Y']:
            return True
        else:
            return False


def Power():
	n = 2
	for x in range(0, 18 + 1):
		print(bin(n ** x))
		yield n ** x
		
def count():
	c = 1
	max = 2 ** 17
	while c < max:
		yield c
		c  <<= 1
		
def Choose(bs: int, rs: RubiksState) -> RubiksState:
	if (bs % 2 ** 18) == 0:
		#Binv
		state = rs.Binv()
		return state
	elif (bs % 2 ** 17) == 0:
		#B2
		pass
	elif (bs % 2 ** 16) == 0:
		#B
		state = rs.B()
		return state
		pass
	elif (bs % 2 ** 15) == 0:
		#Finv
		state = rs.Finv()
		return state
		pass
	elif (bs % 2 ** 14) == 0:
		#F2
		pass
	elif (bs % 2 ** 13) == 0:
		#F
		state = rs.F()
		return state
		pass
	elif (bs % 2 ** 12) == 0:
		#Dinv
		state = rs.Dinv()
		return state
		pass
	elif (bs % 2 ** 11) == 0:
		#D2
		pass
	elif (bs % 2 ** 10) == 0:
		#D
		state = rs.D()
		return state
		pass
	elif (bs % 2 ** 9) == 0:
		#Uinv
		state = rs.Uinv()
		return state
		pass
	elif (bs % 2 ** 8) == 0:
		#U2
		pass
	elif (bs % 2 ** 7) == 0:
		#U
		state = rs.U()
		return state
	elif (bs % 2 ** 6) == 0:
		#Rinv
		state = rs.Rinv()
		return state
		pass
	elif (bs % 2 ** 5) == 0:
		#R2
		pass
	elif (bs % 2 ** 4) == 0:
		#R
		state = rs.R()
		return state
		pass
	elif (bs % 2 ** 3) == 0:
		#Linv
		state = rs.Linv()
		print(state.moves)
		return state
	elif (bs % 2 ** 2) == 0:
		#L2
		pass
	elif (bs % 2 ** 1) == 0:
		#L
		state = rs.L()
		print(state.moves)
		return state
	else:
		pass
	
	
def Charles():
    States = deque([])
#    n = RubiksState(['O', 'B', 'Y'], ['R', 'B', 'Y', ], ['O', 'G', 'Y'], ['R', 'G', 'Y'], ['O', 'B', 'W'], ['R', 'B', 'W'], ['O', 'G', 'W'], ['R', 'G', 'W'], [])
#    rs = RubiksState(["W", "O", "G"], ["G", "W", "R"],  ["R", "Y", "G"], ["Y", "B", "R"], ["R", "W", "B"], ["Y", "G", "O"], ["W", "B", "O"], ["Y", "B", "O"], [])
    rs = RubiksState(["W", "O", "G"], ["Y", "O", "G"],  ["W", "R", "G"], ["Y", "R", "G"], ["W", "G", "O"], ["Y", "G", "O"], ["W", "B", "O"], ["Y", "R", "B"], [])
    L = []
    for e in Power():
    	L.append(e)
    print(L)
    for const in L:
    	choice = Choose(const, rs)
    	if choice != None:
 	   	States.append(choice)
    print(States)
    liszt = []
    for i in L:
    	for j in L:
    		liszt.append((i, j),)
#    liszt = [(x, y) for x, y in zip(L, L)]
    print("Liszt: {}".format(liszt))
    graph = GraphAdjList()
    graph.initialize(L, [(x, y) for x, y in zip(L, L)])
    for e in States:
    	graph.get_neighbors(e)
    print(graph.adj_list)
#    for u in graph.adj_list:
#    	print(u.moves, u.is_solved())
#    	print(i.moves, i.is_solved())
#    print(graph.get_neighbors('A'))
#    print(graph.edge_exists('A', 'B'))
#    print(graph.edge_exists('A', 'E'))
#    graph.remove_edge('A', 'B')
#    print(graph.edge_exists('A', 'B'))
#    graph.add_edge('A', 'B')
#    print(graph.edge_exists('A', 'B'))
#    graph.delete_vertex('A')
#    print(graph.adj_list)

#    L = []
#    for e in Power():
#    	L.append(e)
#    print(L)
#    for const in L:
#    	choice = Choose(const, rs)
#    	if choice != None:
# 	   	States.append(choice)
#    print(States)
#    for s in States:
#    	print("Moves: {}".format(s.moves))
#    	print("State: {}".format(s.orientation))
#    while States:
#    	elem = States.popleft()
#    	if elem.is_solved() == True:
#    		break
#    	else:
#    		for const in L:
#    			choice = Choose(const, elem)
#    			if choice != None:
#    				States.append(choice)


Charles()