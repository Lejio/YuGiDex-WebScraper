from yugiparser import YuGiParser

if __name__ == "__main__":
    
    string = """
                    <div class="search-result__content" tabindex="0"><a
                        href="/product/253906/yugioh-maximum-gold-el-dorado-blue-eyes-white-dragon?xid=pib9534339-5c8e-40d8-aece-00b029258c62&amp;page=1"
                        class="" data-testid="search-result__image--0" tabindex="-1">
                        <section class="search-result__product"><!---->
                          <section class="search-result__image">
                            <div class="lazy-image__wrapper" data-v-6b788ed8=""><img
                                src="https://product-images.tcgplayer.com/fit-in/200x279/253906.jpg"
                                data-testid="product-image__container--Blue-Eyes White Dragon"
                                alt="Blue-Eyes White Dragon" class="v-lazy-image v-lazy-image-loaded"
                                data-v-6b788ed8=""><!----></div>
                          </section><span class="search-result__category-name">YuGiOh</span><span
                            class="search-result__subtitle">Maximum Gold: El Dorado</span>
                          <section class="search-result__rarity"><span>Premium Gold Rare</span><span> ·
                            </span><span>#MGED-EN001</span></section><span class="search-result__title">Blue-Eyes White
                            Dragon</span>
                          <div class="inventory" data-v-66c16b62="">
                            <div class="inventory__container" data-v-66c16b62=""><span
                                class="inventory__listing-count inventory__listing-count-block" data-v-66c16b62=""><span
                                  data-v-66c16b62="">129 listings</span> as low as </span><span class="inventory__price"
                                data-v-66c16b62=""><span class="inventory__price-with-shipping"
                                  data-v-66c16b62="">$1.25</span></span><!----></div>
                          </div><!---->
                          <section class="search-result__market-price"><!---->
                            <section><span>Market Price:</span><span class="search-result__market-price--value"
                                tabindex="-1">$2.30</span></section>
                          </section>
                        </section>
                      </a><!----><!----></div>
    """
    
    
    parse = YuGiParser()
    parse.feed(string)    
    print(parse.getResponse())
    print(parse.getLink())
    parse.close()