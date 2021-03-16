for f in `ls *html`
do
  new="${f}_new"
  cat $f |sed "s/old/new/p" > $new
  mv $new $f
done

