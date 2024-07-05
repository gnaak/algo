select a.ITEM_ID,a.ITEM_NAME,a.RARITY
from ITEM_INFO AS a
left join ITEM_TREE AS b
on a.ITEM_ID = b.PARENT_ITEM_ID
where b.ITEM_ID is null
order by a.ITEM_ID desc