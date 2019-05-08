import sys

sigma = 5
BLOSUM62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}

def linearSpaceGlobalAlignment( v, w, matrix, sigma ):

    def middleColumnScore( v, w, matrix, sigma ):    
        S = [[i*j*sigma for j in xrange(-1, 1)] for i in xrange(len(v)+1)]
        S[0][1] = -sigma
        backtrack = [0]*(len(v)+1)
        for j in xrange(1, len(w)/2+1):
            for i in xrange(0, len(v)+1):
                if i == 0:
                    S[i][1] = -j*sigma
                else:
                    scores = [S[i-1][0] + matrix[v[i-1]][w[j-1]], S[i][0] - sigma, S[i-1][1] - sigma]
                    S[i][1] = max(scores)
                    backtrack[i] = scores.index(S[i][1])
            if j != len(w)/2:
                S = [[row[1]]*2 for row in S]
        return [row[1] for row in S], backtrack
    
    def middleEdge( v, w, matrix, sigma ):
        sourceToMiddle = middleColumnScore(v, w, matrix, sigma)[0]
        middleToSink, backtrack = map(lambda l: l[::-1], middleColumnScore(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1], matrix, sigma))
        scores = map(sum, zip(sourceToMiddle, middleToSink))
        maxMiddle = max(xrange(len(scores)), key=lambda i: scores[i])
        if maxMiddle == len(scores) - 1:
            nextNode = (maxMiddle, len(w)/2 + 1)
        else:
            nextNode = [(maxMiddle + 1, len(w)/2 + 1), (maxMiddle, len(w)/2 + 1), (maxMiddle + 1, len(w)/2),][backtrack[maxMiddle]]
        return (maxMiddle, len(w)/2), nextNode
    
    def globalAlignment( v, w, matrix, sigma ):
        S = [[0 for repeat_j in xrange(len(w)+1)] for repeat_i in xrange(len(v)+1)]
        backtrack = [[0 for repeat_j in xrange(len(w)+1)] for repeat_i in xrange(len(v)+1)]
        for i in xrange(1, len(v)+1):
            S[i][0] = -i*sigma
        for j in xrange(1, len(w)+1):
            S[0][j] = -j*sigma
        for i in xrange(1, len(v)+1):
            for j in xrange(1, len(w)+1):
                scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + matrix[v[i-1], w[j-1]]]
                S[i][j] = max(scores)
                backtrack[i][j] = scores.index(S[i][j])
        insert_indel = lambda word, i: word[:i] + '-' + word[i:]
        vAligned, wAligned = v, w
        i, j = len(v), len(w)
        maxScore = str(S[i][j])
        while i*j != 0:
            if backtrack[i][j] == 0:
                i -= 1
                wAligned = insert_indel(wAligned, j)
            elif backtrack[i][j] == 1:
                j -= 1
                vAligned = insert_indel(vAligned, i)
            else:
                i -= 1
                j -= 1
        for repeat in xrange(i):
            wAligned = insert_indel(wAligned, 0)
        for repeat in xrange(j):
            vAligned = insert_indel(vAligned, 0)
        return maxScore, vAligned, wAligned

    def linearSpaceAlignment( top, bottom, left, right ):
        if left == right:
            return [v[top:bottom], '-'*(bottom - top)]
        elif top == bottom:
            return ['-'*(right - left), w[left:right]]
        elif bottom - top == 1 or right - left == 1:
            return globalAlignment(v[top:bottom], w[left:right], matrix, sigma)[1:]
        else:
            midNode, nextNode = middleEdge(v[top:bottom], w[left:right], matrix, sigma)
            midNode = tuple(map(sum, zip(midNode, [top, left])))
            nextNode = tuple(map(sum, zip(nextNode, [top, left])))
            current = [['-', v[midNode[0] % len(v)]][nextNode[0] - midNode[0]], ['-', w[midNode[1] % len(w)]][nextNode[1] - midNode[1]]]
            A = linearSpaceAlignment(top, midNode[0], left, midNode[1])
            B = linearSpaceAlignment(nextNode[0], bottom, nextNode[1], right)
            return [A[i] + current[i] + B[i] for i in xrange(2)]
    
    
    vAligned, wAligned = linearSpaceAlignment(0, len(v), 0, len(w))
    score = sum([-sigma if '-' in pair else matrix[pair] for pair in zip(vAligned, wAligned)])
    return str(score), vAligned, wAligned

if __name__ == '__main__':
    with open(sys.argv[1]) as input:
        word1, word2 = [line.strip() for line in input.readlines()]
    alignment = linearSpaceGlobalAlignment(word1, word2, BLOSUM62, 5)
    print '\n'.join(alignment)