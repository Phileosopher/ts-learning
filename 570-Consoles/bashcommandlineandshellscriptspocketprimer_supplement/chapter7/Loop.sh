awk '
BEGIN {
  for(i=0; i<5; i++) {
    printf("%3d", i)
  }
}
'
