DOG=$1
if [ $DOG == DACHSHUND ]; then
    echo "You selected DACHSHUND!"
elif [ $DOG == GOLDENRETRIEVER ]; then
    echo "You selected GOLDEN RETRIEVER!"
elif [ $DOG == POMERANIAN ]; then
    echo "You selected POMERANIAN!"
else
    echo "You selected other Dog!"
fi