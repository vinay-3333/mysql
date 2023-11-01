





cur.execute("""
            select * from movie
            where score=(select max(score) from movie)
""")
cur.execute("""select * from movie
            where (gross-budget) = (select max(gross-budget) from movie)
""")

cur.execute("""select count(*) from movie
            where score > (select avg(score) from movie)
""")

cur.execute("""select * from movie
            where year=2000 and score =(select max(score) 
                                        from movie
                                        where year=2000)
""")

cur.execute("""select * from movie
            where score = (select max(score) from movie
                            where votes >(select avg(votes)from movie))""")

cur.execute("""select * from users
            where user_id not in (select distinct(user_id) from orders)
""")


cur.execute("""select * from movie
            where director in (select director form movie
                                group by director
                                order by sum(gross)
                                limit 3)
""")

cur.execute("""select * from movie
            where star in (select star from moviesw
                            where votes > 25000
                            group by star
            having avg(score)>8.5 and votes >25000)
""")


cur.execute("""sekct * from movies 
            where (year,gross-budget) in (select year,max(gross-budget)
                                            from movie
                                            group by year)
""")

cur.execute("""select * from movie
            where (genre,score) in (select genre,max(score)
                                    from movie where votes >25000
                                    group by genre)
""")



cur.execute("""with fav_food as (select name,f_name,count(*) as 'frequency' from users t1
            join orders t2 on t1.user_id = t2.user_id
            join order_details t3 on t2.order_id = t3.order_id
            join food t4 on t3.f_id = t4.f_id
            group by t2.user_id ,t3.f_id)
""")


cur.execute("""select * from fav_food f1
            where frequeny = (selct max(frequeny)
                                from fav_food f2
            where f2.user_id = f1.user_id)
""")


cur.execute("""select name,genre,score,(
            select avg(score)from movie m2 where m2.genre = m1.genre
            )
            from movie m1
""")

cur.execute("""select r_name,avg_rating
            from (select r_id ,avg(restaurant_rating ) as 'avg_rating'
                from order 
                group by r_id ) t1 join testaurants t2
            on t1.r_id = t2.r_id
            )
""")