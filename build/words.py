W = """
anchor apple arrow attic acorn amber anvil album alley anchorage apron arcade ash aspen atlas avenue
bacon badge bagel balcony bamboo banjo barley basin basket beacon beetle bellow bench berry bicycle birch
biscuit bishop blanket blossom bobbin bonfire bookcase boulder bracket branch bridge bucket buffalo bugle bundle burrow
cabin cactus camel candle canoe canvas canyon caramel cargo carpet carrot castle cavern cedar cellar chalk
chapel cheese cherry chimney chisel cider cinder circus cliff clover cobweb cocoa collar comet compass copper
coral cottage cotton crane crater crayon creek crescent cricket crumb crystal cucumber curtain cushion cymbal cypress
daisy dancer dawn deckchair delta denim desert diamond dinghy dolphin domino doorway dragon drawer drizzle drum
dumpling dune dusk eagle easel echo elbow ember emerald engine envelope eucalyptus falcon fennel fern ferry
fiddle fig filter finch fireplace flannel flask flint flounder flute foghorn forest fountain fox freckle frost
galley garden garlic gazelle geyser ginger glacier glider granite grapefruit gravel grotto guitar gull gutter hammock
harbour harp harvest hazel heather hedgehog helmet heron hickory hillside hinge hollow honey hornet horizon hummingbird
hurdle hyacinth iceberg icicle igloo indigo ink iris island ivory jacket jaguar jasmine jetty jigsaw juniper
kayak kennel kernel kettle keyhole kingfisher kitchen kite knapsack knitting koala lagoon lantern larch lattice lavender
ledge lemon lentil leopard lettuce lighthouse lilac linen lobster locket lodge lotus lumber lupin lyric magnet
mallard mandolin mango maple marble marigold marsh meadow medal melon meteor mitten moat mohair molasses monsoon
moorland mosaic moss mountain muffin mulberry mushroom mussel nectar needle nest nettle nickel nightfall notebook nutmeg
oasis oatmeal obelisk ocean octave olive onyx opal orbit orchard orchid otter outcrop overcoat owl
oyster paddle pagoda palette pancake papaya paprika parade parchment parsnip pasture peacock pebble pelican penguin peony
pepper perch petal pewter pheasant piano pigeon pillar pilot pineapple pistachio pitcher plateau platform plover plum
polar pollen pomelo poncho poplar poppy porch portrait postcard pottery prairie pretzel primrose puffin pumpkin purse
quarry quartz quaver quilt quiver radish raft rainbow rampart raven ravine razor reed reef reindeer ribbon
ridge rigging ripple river riverbank robin rocket rosemary rowan rucksack rudder ruffle rug runway saddle saffron
sage sailcloth salmon saltmarsh sandal sapling sapphire sardine satchel saucer sawdust scallop scarf schooner scissors scone
scooter seagull seashell seaweed sesame shallot shamrock shingle shipyard shoreline shovel shrimp shutter sickle silo silver
siren skillet skylark slate sleigh slipper snowdrift sofa sorrel spade sparrow spice spindle spinnaker spire splinter
sponge spoon spruce squirrel stable stadium stallion starfish steeple stepladder stirrup stonework stork stove stream sugar
sultana summit sunflower sunrise surfboard swallow swan sycamore syrup tadpole tambourine tangerine tankard tapestry tarragon teapot
telescope tent terrace thicket thimble thistle thorn thread thunder thyme tiger timber toadstool toboggan tomato topaz
torch tortoise tower trellis triangle trombone trout trowel trumpet tulip tundra tunnel turbine turnip turquoise turtle
twilight umbrella urchin valley vanilla velvet vineyard viola violet vulture waffle wagon walnut walrus warehouse waterfall
weasel weathervane whale wheat whisker whistle willow windmill window wingspan winter wisteria wombat woodland wren yacht
yarn yeast yew yoghurt zebra zinc zinnia zither abbey airfield almond anorak antler apricot aquarium arbour
armchair aubergine avalanche awning balsam banner barge barnacle bassoon bay beanstalk bedrock beehive beret bistro blackbird
"""
ws = W.split()
seen=[]; 
for w in ws:
    if w not in seen: seen.append(w)
print("raw:",len(ws),"unique:",len(seen))
print("need 512 ->", 512-len(seen))
bad=[w for w in seen if not w.isalpha() or not (3<=len(w)<=12)]
print("bad:",bad[:10])
